# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from ncapp.functions import functions

#Modelos generales.
class BaseModel(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta:
 		abstract = True
		permissions = (
			("puede_ver","puede ver"),
		) 

	def __unicode__(self):
		return self.nombre

class Provincia(BaseModel):
    iniciales = models.CharField(max_length=4)

class Municipio(BaseModel):
    provincia = models.ForeignKey(Provincia)

class Empresa(models.Model):
	nit = models.CharField(max_length=255, unique=True)
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	esContratista = models.BooleanField(default=False)
	esContratante = models.BooleanField(default=False)
  
	class Meta:
		permissions = (
			("can_see","can see"),
		) 

	def __unicode__(self):
		return self.nombre

class Cargo(BaseModel):
	empresa = models.ForeignKey(Empresa)
	firma_cartas = models.BooleanField(default=False)

	class Meta:
		permissions = (
			("can_see_cargo","can see cargo"),
		) 

class Funcionario(models.Model):
	empresa = models.ForeignKey(Empresa,related_name="empresa_funcionario",on_delete=models.PROTECT)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	cargo = models.ForeignKey(Cargo,related_name="cargo_funcionario",on_delete=models.PROTECT)
	iniciales = models.CharField(max_length=20,blank=True,null=True)
	activo=models.BooleanField(default=True)

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

	class Meta:
		permissions = (
			("can_see_funcionario","can see funcionario"),
		) 
