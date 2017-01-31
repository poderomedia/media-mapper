from django.db import models
from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
import csv
from django.utils import timezone
from medioschile.models import *
# from medioschile.forms import *
# from medioschile.forms import ContactoForm
# from django.core.mail import send_mail

def index(request):
	articulos = Articulo.objects.filter(destacado = 1)
	articuloscl = articulos.filter(pais__paissociedad = "Chile")
	return render(request, 'medioschile/index.html', {"articuloscl":articuloscl})

class EscritoList(ListView):
	model = Escrito
	context_object_name = 'escrito_list'
	template_name = 'medioschile/escrito_list.html'

class EscritoDetail(DetailView):
	model = Escrito
	context_object_name = 'escrito_detail'
	template_name = 'medioschile/escrito_detail.html'

class CanalTVList(ListView):
	model = CanalTV
	context_object_name = 'canaltv_list'
	template_name = 'medioschile/canaltv_list.html'

class CanalTVDetail(DetailView):
	model = CanalTV
	context_object_name = 'canaltv_detail'
	template_name = 'medioschile/canaltv_detail.html'

class RadioList(ListView):
	model = Radio
	context_object_name = 'radio_list'
	template_name = 'medioschile/radio_list.html'

class RadioDetail(DetailView):
	model = Radio
	context_object_name = 'radio_detail'
	template_name = 'medioschile/radio_detail.html'

class MedioDigitalList(ListView):
	model = MedioDigital
	context_object_name = 'mediodigital_list'
	template_name = 'medioschile/mediodigital_list.html'

class MedioDigitalDetail(DetailView):
	model = MedioDigital
	context_object_name = 'mediodigital_detail'
	template_name = 'medioschile/mediodigital_detail.html'

class PropietarioDetail(DetailView):
	model = Propietario
	context_object_name = 'propietario_detail'
	template_name = 'medioschile/propietario_detail.html'

class PropietarioList(ListView):
	model = Propietario
	context_object_name = 'propietario_list'
	template_name = 'medioschile/propietario_list.html'

class GrupoDetail(DetailView):
	model = Grupo
	context_object_name = 'grupo_detail'
	template_name = 'medioschile/grupo_detail.html'

class GrupoList(ListView):
	model = Grupo
	context_object_name = 'grupo_list'
	template_name = 'medioschile/grupo_list.html'

class RegulacionDetail(DetailView):
	model = Regulacion
	context_object_name = 'regulacion_detail'
	template_name = 'medioschile/regulacion_detail.html'

class RegulacionList(ListView):
	model = Regulacion
	context_object_name = 'regulacion_list'
	template_name = 'medioschile/regulacion_list.html'

class FuenteList(ListView):
	model = Fuente
	context_object_name = 'fuente_list'
	template_name = 'medioschile/fuente_list.html'

'''
def contacto(request):
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			su_nombre = form.cleaned_data['su_nombre']
			asunto = form.cleaned_data['asunto']
			mensaje = form.cleaned_data['mensaje']
			email = form.cleaned_data['email']
			recipients = ['felipe.perry@gmail.com','miguel@poderopedia.com']
		return HttpResponse()
	else:
		form = ContactoForm()
	return render(request, 'medioschile/contacto.html', {'form': form})
'''

