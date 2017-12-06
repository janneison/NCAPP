# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from parametrizacion.models import Provincia, Municipio, Empresa, Cargo, Funcionario

class AdminProvincia(admin.ModelAdmin):
	list_display=('nombre','iniciales')
	search_fields=('nombre','iniciales')	

class AdminMunicipio(admin.ModelAdmin):
	list_display=('nombre','provincia')
	search_fields=('nombre','provincia')	

class AdminEmpresa(admin.ModelAdmin):
	list_display=('rnc','nombre')
	search_fields=('rnc','nombre')

class AdminCargo(admin.ModelAdmin):
	list_display=('nombre','empresa')
	search_fields=('nombre','empresa')	

class AdminFuncionario(admin.ModelAdmin):
	list_display=('cargo','user')
	search_fields=('cargo','user')

admin.site.register(Provincia,AdminProvincia)
admin.site.register(Municipio,AdminMunicipio)
admin.site.register(Empresa,AdminEmpresa)
admin.site.register(Cargo,AdminCargo)
admin.site.register(Funcionario,AdminFuncionario)