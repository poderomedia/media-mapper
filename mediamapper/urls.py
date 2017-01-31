from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import forms_builder.forms.urls


urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS admin
    url(r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^select2/', include('select2.urls')), # select2 multiselect admin
    url(r'^mapademedios/', include('home.urls', namespace='home')), # home
    url(r'^home/', include('home.urls', namespace='home')), # home
    url(r'^medioschile/', include('medioschile.urls', namespace='medioschile')), # medioschile
    url(r'^medioscolombia/', include('medioscolombia.urls', namespace='medioscolombia')), # medioscolombia
    url(r'^mediosargentina/', include('mediosargentina.urls', namespace='mediosargentina')), # medioscolombia
    url(r'^redactor/', include('redactor.urls')), # redactor editor
    url(r'^search/', include('haystack.urls')),
    url(r'^forms/', include(forms_builder.forms.urls)),

)	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)