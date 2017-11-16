# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from models import Provincia, Municipio, Empresa, Cargo
from ncapp.resource import MessageNC, ResponseNC
from serializers import UserSerializer, GroupSerializer, ProvinciaSerializer, MunicipioSerializer, EmpresaSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
	"""
	Retorna una lista de provincias, puede utilizar el parametro (dato) por medio del cual, se podra buscar por todo o parte del nombre, tambien puede ser buscado por sus iniciales.
	"""
	model=Provincia
	queryset = model.objects.all()
	serializer_class = ProvinciaSerializer

	def retrieve(self,request,*args, **kwargs):
		try:
			instance = self.get_object()
			serializer = self.get_serializer(instance)
			return Response({ResponseNC.message:'',ResponseNC.status:'success',ResponseNC.data:serializer.data})
		except:
			return Response({ResponseNC.message:MessageNC['vacio'],'success':'fail',ResponseNC.data:''},status=status.HTTP_404_NOT_FOUND)


	def list(self, request, *args, **kwargs):
		try:
			queryset = super(ProvinciaViewSet, self).get_queryset()
			dato = self.request.query_params.get('dato', None)
			if dato:
				qset = (
					Q(nombre__icontains=dato)|
					Q(iniciales__icontains=dato)
					)
				queryset = self.model.objects.filter(qset)
			#utilizar la variable ignorePagination para quitar la paginacion
			ignorePagination= self.request.query_params.get('ignorePagination',None)
			if ignorePagination is None:
				page = self.paginate_queryset(queryset)
				if page is not None:
					serializer = self.get_serializer(page,many=True)	
					return self.get_paginated_response({ResponseNC.message:'','success':'ok',
					ResponseNC.data:serializer.data})
	
			serializer = self.get_serializer(queryset,many=True)
			return Response({ResponseNC.message:'','success':'ok',
					ResponseNC.data:serializer.data})			
		except:
			return Response({ResponseNC.message:MessageNC['errorServidor'],ResponseNC.status:'error',ResponseNC.data:''},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


	def create(self, request, *args, **kwargs):
		if request.method == 'POST':
			try:
				serializer = ProvinciaSerializer(data=request.DATA,context={'request': request})

				if serializer.is_valid():
					serializer.save()
					return Response({ResponseNC.message:'El registro ha sido guardado exitosamente','success':'ok',
						ResponseNC.data:serializer.data},status=status.HTTP_201_CREATED)
				else:
				 	return Response({ResponseNC.message:'datos requeridos no fueron recibidos','success':'fail',
			 		ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)
			except:
			 	return Response({ResponseNC.message:'Se presentaron errores al procesar los datos','success':'error',
			  		ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)

	def update(self,request,*args,**kwargs):
		if request.method == 'PUT':
			try:
				partial = kwargs.pop('partial', False)
				instance = self.get_object()
				serializer = ProvinciaSerializer(instance,data=request.DATA,context={'request': request},partial=partial)
				if serializer.is_valid():
					self.perform_update(serializer)
					return Response({ResponseNC.message:'El registro ha sido actualizado exitosamente','success':'ok',
						ResponseNC.data:serializer.data},status=status.HTTP_201_CREATED)
				else:
				 	return Response({ResponseNC.message:'datos requeridos no fueron recibidos','success':'fail',
			 		ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)
			except:
			 	return Response({ResponseNC.message:'Se presentaron errores al procesar los datos','success':'error',
					ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)

	def destroy(self,request,*args,**kwargs):
		try:
			instance = self.get_object()
			self.perform_destroy(instance)
			return Response({ResponseNC.message:'El registro se ha eliminado correctamente','success':'ok',
				ResponseNC.data:''},status=status.HTTP_204_NO_CONTENT)
		except:
			return Response({ResponseNC.message:'Se presentaron errores al procesar la solicitud','success':'error',
			ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)	

class MunicipioViewSet(viewsets.ModelViewSet):
	"""
	Retorna una lista de Municipios, puede utilizar el parametro (dato) a traver del cual, se podra buscar por todo o parte del nombre, tambien puede buscar los municipios que hacen parte de determinado provincia.
	"""
	model=Municipio
	queryset = model.objects.all()
	serializer_class = MunicipioSerializer

	def retrieve(self,request,*args, **kwargs):
		try:
			instance = self.get_object()
			serializer = self.get_serializer(instance)
			return Response({ResponseNC.message:'',ResponseNC.status:'success',ResponseNC.data:serializer.data})
		except:
			return Response({ResponseNC.message:'No se encontraron datos','success':'fail',ResponseNC.data:''},status=status.HTTP_404_NOT_FOUND)


	def list(self, request, *args, **kwargs):
		try:
			queryset = super(MunicipioViewSet, self).get_queryset()
			dato = self.request.query_params.get('dato', None)
			id_provincia= self.request.query_params.get('id_provincia', None)
			
			if dato or id_provincia:
				if dato:
					qset = (
						Q(nombre__icontains=dato)|
						Q(nit__icontains=dato)
						)
				if id_provincia:
					if dato:
						qset=qset&(Q(provincia_id=id_provincia))
					else:
						qset=(Q(provincia_id=id_provincia))
						

				queryset = self.model.objects.filter(qset)
			#utilizar la variable ignorePagination para quitar la paginacion
			ignorePagination= self.request.query_params.get('ignorePagination',None)
			if ignorePagination is None:
				page = self.paginate_queryset(queryset)
				if page is not None:
					serializer = self.get_serializer(page,many=True)	
					return self.get_paginated_response({ResponseNC.message:'','success':'ok',
					ResponseNC.data:serializer.data})
	
			serializer = self.get_serializer(queryset,many=True)
			return Response({ResponseNC.message:'','success':'ok',
					ResponseNC.data:serializer.data})

		except:
			return Response({ResponseNC.message:'Se presentaron errores de comunicacion con el servidor',ResponseNC.status:'error',ResponseNC.data:''},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	def create(self, request, *args, **kwargs):
		if request.method == 'POST':
			try:
				serializer = MunicipioSerializer(data=request.DATA,context={'request': request})

				if serializer.is_valid():
					serializer.save(provincia_id=request.DATA['provincia_id'])
					return Response({ResponseNC.message:'El registro ha sido guardado exitosamente','success':'ok',
						ResponseNC.data:serializer.data},status=status.HTTP_201_CREATED)
				else:
				 	return Response({ResponseNC.message:'datos requeridos no fueron recibidos','success':'fail',
			 		ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)
			except:
			 	return Response({ResponseNC.message:'Se presentaron errores al procesar los datos','success':'error',
			  		ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)

	def update(self,request,*args,**kwargs):
		if request.method == 'PUT':
			try:
				partial = kwargs.pop('partial', False)
				instance = self.get_object()
				serializer = MunicipioSerializer(instance,data=request.DATA,context={'request': request},partial=partial)
				if serializer.is_valid():
					self.perform_update(serializer)
					return Response({ResponseNC.message:'El registro ha sido actualizado exitosamente','success':'ok',
						ResponseNC.data:serializer.data},status=status.HTTP_201_CREATED)
				else:
				 	return Response({ResponseNC.message:'datos requeridos no fueron recibidos','success':'fail',
			 		ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)
			except:
			 	return Response({ResponseNC.message:'Se presentaron errores al procesar los datos','success':'error',
					ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)

	def destroy(self,request,*args,**kwargs):
		try:
			instance = self.get_object()
			self.perform_destroy(instance)
			return Response({ResponseNC.message:'El registro se ha eliminado correctamente','success':'ok',
				ResponseNC.data:''},status=status.HTTP_204_NO_CONTENT)
		except:
			return Response({ResponseNC.message:'Se presentaron errores al procesar la solicitud','success':'error',
			ResponseNC.data:''},status=status.HTTP_400_BAD_REQUEST)
#Fin api rest para municipio
