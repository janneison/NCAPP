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

class Estado(BaseModel):
    descripcion = models.CharField(max_length=500)

class Proyecto(BaseModel):
    convenio = models.ForeignKey(Convenio)
    empresa = models.ForeignKey(Empresa, null=True)
    estado = models.ForeignKey(Estado, null=True)

class Poligono(BaseModel):
    lote = models.ForeignKey(Proyecto, null=True)

class Circuito(BaseModel):
    lote = models.ManyToManyField(Proyecto, null=True)

class Apoyo(BaseModel):
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    lote = models.ManyToManyField(Proyecto)

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

    def __str__(self):
		return self.capitulo.nombre + ' ' + self.nombre

class Levantamiento(BaseModel):
    municipio = models.ForeignKey(Municipio)
    apoyo = models.ForeignKey(Apoyo)
    version = models.ForeignKey(Version)
    contratista 	= models.ForeignKey(Empresa, related_name='fk_contratista', on_delete=models.PROTECT)
    fecha 	= models.DateField(blank=True, null=True)
    poligono = models.ForeignKey(Poligono, null=True)
    observacion = models.CharField(max_length=500)
    longitudPlano = models.DecimalField(default=0,max_digits=19,decimal_places=2)
    terreno = models.DecimalField(default=0,max_digits=19,decimal_places=2)
    soporte = models.FileField(upload_to = 'soporteLEV',null=True)

class DetalleLevantamiento(models.Model):
    valores = ((u'C',u'Conforme'),(u'NC',u'NoConforme'),
		(u'N/A',u'No Aplica'),)
    levantamiento = models.ForeignKey(Levantamiento)
    actividad = models.ForeignKey(Actividad)
    valor = models.CharField(max_length=50,choices=valores,default='N/A')

    def __str__(self):
        return self.actividad.nombre

class SoporteNC(models.Model):
    detalleLevantamiento = models.ForeignKey(DetalleLevantamiento)
    soporte = models.FileField(upload_to = 'soporteNC')
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion









