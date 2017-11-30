from __future__ import unicode_literals

from django.contrib import admin
from levantamiento.models import (Proyecto, Convenio, 
Circuito, Apoyo, Version, TipoDato, Capitulo, 
Levantamiento, Estado, DetalleLevantamiento,SoporteNC,
Norma, Defecto, Actividad)

class AdminConvenio(admin.ModelAdmin):
	list_display=('nombre','descripcion')
	search_fields=('nombre','descripcion')	

class AdminProyecto(admin.ModelAdmin):
	list_display=('nombre','convenio')
	search_fields=('nombre','convenio')	

class AdminCircuito(admin.ModelAdmin):
	list_display=('nombre',)
	search_fields=('nombre',)

class AdminApoyo(admin.ModelAdmin):
	list_display=('nombre','latitud','longitud')
	search_fields=('nombre',)	

class AdminVersion(admin.ModelAdmin):
	list_display=('version',)
	search_fields=('version',)

class AdminTipoDato(admin.ModelAdmin):
	list_display=('nombre','comportamiento')
	search_fields=('nombre','comportamiento')

class AdminNorma(admin.ModelAdmin):
	list_display=('nombre','capitulo')
	search_fields=('nombre','capitulo')

class AdminDefecto(admin.ModelAdmin):
	list_display=('nombre','capitulo')
	search_fields=('nombre','capitulo')	

class AdminEstado(admin.ModelAdmin):
	list_display=('nombre','descripcion')
	search_fields=('nombre','descripcion')		

admin.site.register(Convenio,AdminConvenio)
admin.site.register(Proyecto,AdminProyecto)
admin.site.register(Circuito,AdminCircuito)
admin.site.register(Apoyo,AdminApoyo)
admin.site.register(Version,AdminVersion)
admin.site.register(TipoDato,AdminTipoDato)
admin.site.register(Norma,AdminNorma)
admin.site.register(Defecto,AdminDefecto)
admin.site.register(Estado,AdminEstado)

class NormaInline(admin.TabularInline):
    model = Norma
    extra = 3
    classes = ['collapse']

class DefectoInline(admin.TabularInline):
    model = Defecto
    extra = 3
    classes = ['collapse']

class ActividadInline(admin.TabularInline):
    model = Actividad
    extra = 3
    classes = ['collapse']
    
class AdminCapitulo(admin.ModelAdmin):
    inlines = [ ActividadInline,NormaInline,DefectoInline ]
    list_display = ('nombre', 'version')
    
admin.site.register(Capitulo, AdminCapitulo)

class DetalleLevantamientoInline(admin.TabularInline):
    model = DetalleLevantamiento
    extra = 3
    classes = ['collapse']
    
class AdminLevantamiento(admin.ModelAdmin):
    inlines = [ DetalleLevantamientoInline ]
    list_display = ('apoyo', 'fecha')
    
admin.site.register(Levantamiento, AdminLevantamiento)

class AdminSoporteNC(admin.ModelAdmin):
	list_display=('nombre','detalleLevantamiento','descripcion')
	search_fields=('nombre','detalleLevantamiento')	

admin.site.register(SoporteNC, AdminSoporteNC)
