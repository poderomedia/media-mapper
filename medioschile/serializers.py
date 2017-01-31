from medioschile.models import Ejecutivo,Empresario,GeneroEscrito,Region,Comuna,Ciudad,Sector,Periodicidad,Propietario,TipoSociedad,PaisSociedad,Sociedad,Grupo,Escrito,GeneroRadio,Radio,GeneroCanalTV,CanalTV,GeneroMedioDigital,MedioDigital,Autor,Fuente,TipoDocumento,Regulacion,CargoEjecutivo,Cargo,Etiqueta,Articulo
from rest_framework import serializers

class PropietarioChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propietario
        fields = ('propietario', 'rutpropietario', 'tiposociedad', 'sociedadcontroladora', 'propietariopropietario')

class TipoSociedadChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoSociedad
        fields = ('tiposociedad',)

class SociedadChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sociedad
        fields = ('sociedad', 'rutsociedad', 'controlador', 'sociedadcontroladora', 'linksociedad')

class GrupoChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo
        fields = ('grupo', 'controladorgrupo', 'paisorigen', 'linkgrupo')

class PaisSociedadChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaisSociedad
        fields = ('paissociedad',)

class RadioChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radio
        fields = ('medio', 'frecuencia', 'genero', 'propietario', 'grupo',  'sitioweb')

class EscritoChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escrito
        fields = ('medio', 'tipo', 'genero', 'propietario', 'grupo',  'sitioweb')

class CanalTVChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CanalTV
        fields = ('medio', 'tipo', 'genero', 'propietario', 'grupo',  'sitioweb')

class MedioDigitalChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedioDigital
        fields = ('medio', 'genero', 'propietario', 'grupo',  'sitioweb')

class GeneroRadioChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroRadio
        fields = ('genero',)

class GeneroCanalTVChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroCanalTV
        fields = ('genero',)

class GeneroEscritoChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroEscrito
        fields = ('genero',)

class GeneroMedioDigitalChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroMedioDigital
        fields = ('genero',)

class FuenteChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fuente
        fields = ('fuente', 'descripcionfuente', 'autor', 'linkfuente')

class ArticuloChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articulo
        fields = ('titulo', 'subtitulo', 'cuerpo', 'fecha', 'autor', 'extracto', 'pais')

class EmpresarioChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresario
        fields = ('empresario', 'linkempresario')

class EjecutivoChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ejecutivo
        fields = ('ejecutivo',)

class AutorChileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('autor',)