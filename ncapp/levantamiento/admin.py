from __future__ import unicode_literals

from django.contrib import admin
from models import Proyecto, Convenio, Circuito, Apoyo, Version, TipoDato

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
	list_display=('nombre','circuito','lote')
	search_fields=('nombre','circuito','lote')	

class AdminVersion(admin.ModelAdmin):
	list_display=('version',)
	search_fields=('version',)

class AdminTipoDato(admin.ModelAdmin):
	list_display=('nombre','comportamiento')
	search_fields=('nombre','comportamiento')	

admin.site.register(Convenio,AdminConvenio)
admin.site.register(Proyecto,AdminProyecto)
admin.site.register(Circuito,AdminCircuito)
admin.site.register(Apoyo,AdminApoyo)
admin.site.register(Version,AdminVersion)
admin.site.register(TipoDato,AdminTipoDato)
