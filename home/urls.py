from . import views
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

urlpatterns = [
	url(r'^index/$', 'home.views.index', name='index'),
    url(r'^api/$', 'home.views.api', name='api'),
    url(r'^acercade/$', 'home.views.acercade', name='acercade'),
    url(r'^consultadirecta/$', 'home.views.consultadirecta', name='consultadirecta'),
    url(r'^metodologia/$', 'home.views.metodologia', name='metodologia'),
    url(r'^privacidad/$', 'home.views.privacidad', name='privacidad'),
    url(r'^datos/$', 'home.views.datos', name='datos'),
    url(r'^codigo/$', 'home.views.codigo', name='codigo'),
    url(r'^contacto/$', 'home.views.contacto', name='contacto'),
    url(r'^aporta/$', 'home.views.aporta', name='aporta'),
    url(r'^analisis/$', views.AnalisisList.as_view(), name='analisislist'),
    url(r'^analisis/(?P<pk>\d+)/$', views.AnalisisDetail.as_view(), name='analisisdetail'),
    url(r'^analisiscl/(?P<pk>\d+)/$', views.AnalisisDetail.as_view(), name='analisisdetailcl'),
    url(r'^analisiscol/(?P<pk>\d+)/$', views.AnalisisDetail.as_view(), name='analisisdetailcol'),
    url(r'^analisiscl/$', 'home.views.analisiscl', name='analisiscl'),
    url(r'^analisiscol/$', 'home.views.analisiscol', name='analisiscol'),
    url(r'^gracias/$', 'home.views.gracias', name='gracias'),
    url(r'^graciascontacto/$', 'home.views.graciascontacto', name='graciascontacto'),
    url(r'^agregarmediodigital/$', 'home.views.agregarmediodigital', name='agregarmediodigital'),
    url(r'^agregarcanaltv/$', 'home.views.agregarcanaltv', name='agregarcanaltv'),
    url(r'^agregarradio/$', 'home.views.agregarradio', name='agregarradio'),
    url(r'^agregarimpreso/$', 'home.views.agregarimpreso', name='agregarimpreso'),
]