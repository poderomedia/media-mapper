from django.db import models
from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from medioscolombia.models import *
from medioschile.models import Articulo

def index(request):
	articulos = Articulo.objects.filter(destacado = 1)
	articuloscol = articulos.filter(pais__paissociedad = "Colombia")
	return render(request, 'medioscolombia/index.html', {"articuloscol":articuloscol})

class EscritoList(ListView):
	model = Escrito
	context_object_name = 'escrito_list'
	template_name = 'medioscolombia/escrito_list.html'

class EscritoDetail(DetailView):
	model = Escrito
	context_object_name = 'escrito_detail'
	template_name = 'medioscolombia/escrito_detail.html'

class CanalTVList(ListView):
	model = CanalTV
	context_object_name = 'canaltv_list'
	template_name = 'medioscolombia/canaltv_list.html'

class CanalTVDetail(DetailView):
	model = CanalTV
	context_object_name = 'canaltv_detail'
	template_name = 'medioscolombia/canaltv_detail.html'

class RadioList(ListView):
	model = Radio
	context_object_name = 'radio_list'
	template_name = 'medioscolombia/radio_list.html'

class RadioDetail(DetailView):
	model = Radio
	context_object_name = 'radio_detail'
	template_name = 'medioscolombia/radio_detail.html'

class MedioDigitalList(ListView):
	model = MedioDigital
	context_object_name = 'mediodigital_list'
	template_name = 'medioscolombia/mediodigital_list.html'

class MedioDigitalDetail(DetailView):
	model = MedioDigital
	context_object_name = 'mediodigital_detail'
	template_name = 'medioscolombia/mediodigital_detail.html'

class PropietarioDetail(DetailView):
	model = Propietario
	context_object_name = 'propietario_detail'
	template_name = 'medioscolombia/propietario_detail.html'

class PropietarioList(ListView):
	model = Propietario
	context_object_name = 'propietario_list'
	template_name = 'medioscolombia/propietario_list.html'

class GrupoDetail(DetailView):
	model = Grupo
	context_object_name = 'grupo_detail'
	template_name = 'medioscolombia/grupo_detail.html'

class GrupoList(ListView):
	model = Grupo
	context_object_name = 'grupo_list'
	template_name = 'medioscolombia/grupo_list.html'

class RegulacionDetail(DetailView):
	model = Regulacion
	context_object_name = 'regulacion_detail'
	template_name = 'medioscolombia/regulacion_detail.html'

class RegulacionList(ListView):
	model = Regulacion
	context_object_name = 'regulacion_list'
	template_name = 'medioscolombia/regulacion_list.html'

class FuenteList(ListView):
	model = Fuente
	context_object_name = 'fuente_list'
	template_name = 'medioscolombia/fuente_list.html'