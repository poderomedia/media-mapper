import django_tables2 as tables
from medioschile.models import Ejecutivo,Empresario,GeneroEscrito,Region,Comuna,Ciudad,Sector,Periodicidad,Propietario,TipoSociedad,PaisSociedad,Sociedad,Escrito,GeneroRadio,Radio,GeneroCanalTV,CanalTV,GeneroMedioDigital,MedioDigital,Autor,Fuente,TipoDocumento,Regulacion

class PapelTable(tables.Table):
	class Meta:
		model = Escrito
		attrs = {"class": "paleblue"}

class CanalTVTable(tables.Table):
	class Meta:
		model = CanalTV
		attrs = {"class": "paleblue"}

class RadioTable(tables.Table):
	class Meta:
		model = Radio
		attrs = {"class": "paleblue"}

class DigitalTable(tables.Table):
	class Meta:
		model = MedioDigital
		attrs = {"class": "paleblue"}