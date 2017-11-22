from __future__ import unicode_literals

from django.contrib import admin
from levantamiento.models import Proyecto, Convenio, Circuito, Apoyo, Version, TipoDato, Capitulo, Norma, Defecto, Actividad

class AdminConvenio(admin.ModelAdmin):
	list_display=('nombre','descripcion')
	search_fields=('nombre','descripcion')	

class AdminProyecto(admin.ModelAdmin):
	list_display=('nombre','convenio')
	search_fields=('nombre','convenio')	

class AdminCircuito(admin.ModelAdmin):
	list_display=('empresa','nombre')
	search_fields=('empresa','nombre')

class AdminApoyo(admin.ModelAdmin):
	list_display=('nombre','circuito')
	search_fields=('nombre','circuito')	

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

admin.site.register(Convenio,AdminConvenio)
admin.site.register(Proyecto,AdminProyecto)
admin.site.register(Circuito,AdminCircuito)
admin.site.register(Apoyo,AdminApoyo)
admin.site.register(Version,AdminVersion)
admin.site.register(TipoDato,AdminTipoDato)
admin.site.register(Norma,AdminNorma)
admin.site.register(Defecto,AdminDefecto)

class ActividadInline(admin.TabularInline):
    model = Actividad
    extra = 3
    classes = ['collapse']
    
class AdminCapitulo(admin.ModelAdmin):
    inlines = [ ActividadInline ]
    list_display = ('nombre', 'version')
    
admin.site.register(Capitulo, AdminCapitulo)
