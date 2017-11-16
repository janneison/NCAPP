from django.contrib.auth.models import User, Group
from rest_framework import serializers
from parametrizacion.models import Provincia, Municipio, Empresa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Provincia
		fields=('id','nombre','iniciales')


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
	esContratista = serializers.BooleanField(default=False)
	esContratante = serializers.BooleanField(default=False)
	#logo = serializers.ImageField(required=False)

	class Meta:
		model = Empresa
		fields=('url','id','nombre','nit','direccion','esContratista','esContratante' )

class MunicipioSerializer(serializers.HyperlinkedModelSerializer):

	provincia_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Provincia.objects.all())
	provincia=ProvinciaSerializer(read_only=True)
	class Meta:
		model = Municipio
		fields=('id','nombre','provincia','provinica_id')

