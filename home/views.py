from django.db import models
from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.template.context_processors import csrf
from medioschile.models import *
from medioscolombia.models import *

def index(request):
	articulos = Articulo.objects.filter(destacado = 1)
	return render(request, 'home/index.html', {"articulos":articulos})

def api(request):
	return render(request, 'home/api.html')

def consultadirecta(request):
	return render(request, 'home/consultadirecta.html')

def metodologia(request):
	return render(request, 'home/metodologia.html')

def datos(request):
	return render(request, 'home/datos.html')

def codigo(request):
	return render(request, 'home/codigo.html')

def analisis(request):
	return render(request, 'home/analisis.html')

def acercade(request):
	return render(request, 'home/acercade.html')

def contacto(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'home/contacto.html',c)

def aporta(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'home/aporta.html',c)

def privacidad(request):
	return render(request, 'home/privacidad.html')

def gracias(request):
	return render(request, 'home/gracias.html')

def graciascontacto(request):
	return render(request, 'home/graciascontacto.html')

class AnalisisList(ListView):
	model = Articulo
	context_object_name = 'analisis_list'
	template_name = 'home/analisis_list.html'

class AnalisisDetail(DetailView):
	model = Articulo
	context_object_name = 'analisis_detail'
	template_name = 'home/analisis_detail.html'

def analisiscl(request):
	analisiscl = Articulo.objects.filter(pais = 1)
	return render(request, 'home/analisis_listcl.html', {"analisiscl":analisiscl})

def analisiscol(request):
	analisiscol = Articulo.objects.filter(pais = 8)
	return render(request, 'home/analisis_listcol.html', {"analisiscol":analisiscol})

def etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'home/analisis_list.html', {"etiquetas":etiquetas})

def agregarmediodigital(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'home/agregarmediodigital.html',c)

def agregarcanaltv(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'home/agregarcanaltv.html',c)

def agregarradio(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'home/agregarradio.html',c)

def agregarimpreso(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'home/agregarimpreso.html',c)