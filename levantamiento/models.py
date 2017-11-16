# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from parametrizacion.models import Empresa, Municipio
from ncapp.functions import functions

#Modelos.
class BaseModel(models.Model):
	nombre = models.CharField(max_length=500)

	class Meta:
 		abstract = True

	def __str__(self):
		return self.nombre

class Convenio(BaseModel):
    descripcion = models.CharField(max_length=500)

class Proyecto(BaseModel):
    convenio = models.ForeignKey(Convenio)

class Circuito(BaseModel):
    empresa = models.ForeignKey(Empresa)

class Apoyo(BaseModel):
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    circuito = models.ForeignKey(Circuito)
    lote = models.ForeignKey(Proyecto, null=True)

class Version(models.Model):
	version = models.CharField(max_length=50) 
    
	def __str__(self):
		return self.version

class TipoDato(BaseModel):
    comportamiento = models.CharField(max_length=500)

class Capitulo(BaseModel):
    alineacion = models.CharField(max_length=50)
    version = models.ForeignKey(Version)

class Norma(BaseModel):
    capitulo = models.ForeignKey(Capitulo)

class Defecto(BaseModel):
    capitulo = models.ForeignKey(Capitulo)

class Actividad(BaseModel):
    capitulo = models.ForeignKey(Capitulo)
    tipoDato = models.ForeignKey(TipoDato)

class Levantamiento(BaseModel):
    empresa = models.ForeignKey(Empresa)
    municipio = models.ForeignKey(Municipio)
    apoyo = models.ForeignKey(Apoyo)
    version = models.ForeignKey(Version)
    contratista 	= models.ForeignKey(Empresa, related_name='fk_contratista', on_delete=models.PROTECT)
    fecha 	= models.DateField(blank=True, null=True)
    inspeccion = models.IntegerField(default=0)
    poligono = models.CharField(max_length=50)
    observacion = models.CharField(max_length=500)

class DetalleLevantamiento(models.Model):
    levantamiento = models.ForeignKey(Levantamiento)
    actividad = models.ForeignKey(Actividad)
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.actividad.nombre

class SoporteNC(models.Model):
    detalleLevantamiento = models.ForeignKey(DetalleLevantamiento)
    soporte = models.FileField(upload_to = 'soporteNC')
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion









