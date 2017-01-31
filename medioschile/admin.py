# -*- encoding: utf-8 -*-
from django.contrib import admin
from django import forms
# from import_export import resources
# from import_export.admin import ImportExportActionModelAdmin
from redactor.widgets import RedactorEditor
from medioschile.models import Ejecutivo,Empresario,GeneroEscrito,Region,Comuna,Ciudad,Sector,Periodicidad,Propietario,TipoSociedad,PaisSociedad,Sociedad,Escrito,GeneroRadio,Radio,GeneroCanalTV,CanalTV,GeneroMedioDigital,MedioDigital,Grupo,Cargo,CargoEjecutivo,Autor,Fuente,TipoDocumento,Regulacion,Articulo,Etiqueta

class ListaEjecutivos(admin.ModelAdmin):
    search_fields = ['ejecutivo']

class ListaEmpresarios(admin.ModelAdmin):
    search_fields = ['empresario']

class ListaRegiones(admin.ModelAdmin):
    search_fields = ['region']

class ListaComunas(admin.ModelAdmin):
    search_fields = ['comuna']

class ListaCiudades(admin.ModelAdmin):
    search_fields = ['ciudad']

class ListaPaises(admin.ModelAdmin):
    search_fields = ['paissociedad']

class ListaSociedades(admin.ModelAdmin):
    search_fields = ['sociedad']
    list_display = ('sociedad','tiposociedad','presidentedirectorio')
    fieldsets = (
        ('Datos de Sociedad', {
            'fields': (('sociedad','tiposociedad'),('rutsociedad','paissocio'),('controlador','presidentedirectorio'),'miembrosdirectorio','sectores','fuentes','linksociedad'),
        }),
        ('Sociedades Propietarias -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('sociedadcontroladora','pcentsociedadcontroladora'),('otrasociedada','pcentsociedada'),('otrasociedadb','pcentsociedadb'),('otrasociedadc','pcentsociedadc'),('otrasociedadd','pcentsociedadd'),('otrasociedade','pcentsociedade'),('otrasociedadf','pcentsociedadf'),('otrasociedadg','pcentsociedadg'),('otrasociedadh','pcentsociedadh'),('otrasociedadi','pcentsociedadi'),('otrasociedadj','pcentsociedadj'),('otrasociedadk','pcentsociedadk'),('otrasociedadl','pcentsociedadl'),('otrasociedadm','pcentsociedadm'),('otrasociedadn','pcentsociedadn'),('fechainfo','fuentesociedad')),
        }),
        ('Utilidades -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('utilidades','infoutilidades','fuenteutilidades'),
        }),
    )

class ListaPropietarios(admin.ModelAdmin):
    search_fields = ['propietario']
    list_display = ('propietario','tiposociedad','presidentedirectorio')
    fieldsets = (
        ('Datos de Propietario', {
            'fields': (('propietario','tiposociedad'),'rutpropietario',('presidentedirectorio'),'miembrosdirectorio','sectores',('propietariopropietario','pcentpropietario'),'observacionespropiedad','fuentepropietario','grupo'),
        }),
        ('Ejecutivos -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('ejecutivouno','ejecutivounocargo','ejecutivounocargofecha'),('ejecutivodos','ejecutivodoscargo','ejecutivodoscargofecha'),('ejecutivotres','ejecutivotrescargo','ejecutivotrescargofecha'),('ejecutivocuatro','ejecutivocuatrocargo','ejecutivocuatrocargofecha'),('ejecutivocinco','ejecutivocincocargo','ejecutivocincocargofecha'),('ejecutivoseis','ejecutivoseiscargo','ejecutivoseiscargofecha')),
        }),
        ('Medios -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('escritospropietario','radiospropietario','canaltvspropietario','digitalespropietario'),
        }),
        ('Sociedades Propietarias -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('sociedadcontroladora','pcentsociedadcontroladora'),('otrasociedada','pcentsociedada'),('otrasociedadb','pcentsociedadb'),('otrasociedadc','pcentsociedadc'),('otrasociedadd','pcentsociedadd'),('otrasociedade','pcentsociedade'),('otrasociedadf','pcentsociedadf'),('otrasociedadg','pcentsociedadg'),('otrasociedadh','pcentsociedadh'),('otrasociedadi','pcentsociedadi'),('otrasociedadj','pcentsociedadj'),('otrasociedadk','pcentsociedadk'),('otrasociedadl','pcentsociedadl'),('otrasociedadm','pcentsociedadm'),('otrasociedadn','pcentsociedadn'),('fechainfo','fuentesociedad')),
        }),
        ('Financistas -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('financistas','infofinancistas','fuentefinancistas'),
        }),
        ('Utilidades -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('utilidades','infoutilidades','fuenteutilidades'),
        }),
    )

class MedioEscritoAdmin(admin.ModelAdmin):
    list_display = ('medio','tipo','genero','periodicidad','inicioyear','circulacion','sitioweb','observaciones','check')
    search_fields = ['medio']
    fieldsets = (
        ('Datos del Medio', {
            'fields': ('medio',('tipo','pagado_gratuito','genero'),('inicio','inicioyear','periodicidad',),('direccion','sitioweb'),'propietario','fuentepropiedad','grupo','logo'),
        }),
        ('Datos de Circulación -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('circulacion','region','comuna','ciudad'),
        }),
        ('Medio Asociado a -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('asociadoaescrito','asociadoaradio','asociadoacanaltv','asociadoamediodigital'),
        }),
        ('Datos de Lectoría y Tiraje -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('lectoria','infolectoria','fuentelectoria','tiraje','infotiraje','fuentetiraje'),
        }),
        ('Extra -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('telefono','observaciones','anexos','check'),
        }),
        ('Ejecutivos -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('ejecutivouno','ejecutivounocargo','ejecutivounocargofecha'),('ejecutivodos','ejecutivodoscargo','ejecutivodoscargofecha'),('ejecutivotres','ejecutivotrescargo','ejecutivotrescargofecha'),('ejecutivocuatro','ejecutivocuatrocargo','ejecutivocuatrocargofecha'),('ejecutivocinco','ejecutivocincocargo','ejecutivocincocargofecha'),('ejecutivoseis','ejecutivoseiscargo','ejecutivoseiscargofecha'),('ejecutivosiete','ejecutivosietecargo','ejecutivosietecargofecha'),('ejecutivoocho','ejecutivoochocargo','ejecutivoochocargofecha'),('ejecutivonueve','ejecutivonuevecargo','ejecutivonuevecargofecha'),('ejecutivodiez','ejecutivodiezcargo','ejecutivodiezcargofecha')),
        }),
    )
    readonly_fields=('app',)
    
class RadiosAdmin(admin.ModelAdmin):
    list_display = ('medio','frecuencia','genero','inicioyear','indiceaudiencia','sitioweb','observaciones','check')
    search_fields = ['medio']
    fieldsets = (
        ('Datos del Medio', {
            'fields': ('medio',('genero','frecuencia'),('inicio','inicioyear'),('direccion','sitioweb'),'propietario','fuentepropiedad','grupo','logo'),
        }),
        ('Datos de Cobertura -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('cobertura','region','comuna','ciudad'),
        }),
        ('Medio Asociado a -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('asociadoaescrito','asociadoaradio','asociadoacanaltv','asociadoamediodigital'),
        }),
        ('Datos de Audiencia -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('indiceaudiencia','infoaudiencia','fuenteaudiencia'),
        }),
        ('Extra -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('telefono','observaciones','anexos','check'),
        }),
        ('Ejecutivos -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('ejecutivouno','ejecutivounocargo','ejecutivounocargofecha'),('ejecutivodos','ejecutivodoscargo','ejecutivodoscargofecha'),('ejecutivotres','ejecutivotrescargo','ejecutivotrescargofecha'),('ejecutivocuatro','ejecutivocuatrocargo','ejecutivocuatrocargofecha'),('ejecutivocinco','ejecutivocincocargo','ejecutivocincocargofecha'),('ejecutivoseis','ejecutivoseiscargo','ejecutivoseiscargofecha'),('ejecutivosiete','ejecutivosietecargo','ejecutivosietecargofecha'),('ejecutivoocho','ejecutivoochocargo','ejecutivoochocargofecha'),('ejecutivonueve','ejecutivonuevecargo','ejecutivonuevecargofecha'),('ejecutivodiez','ejecutivodiezcargo','ejecutivodiezcargofecha')),
        }),
    )
    readonly_fields=('app',)

class CanalesTVAdmin(admin.ModelAdmin):
    list_display = ('medio','tipo','genero','inicioyear','rating','sitioweb','observaciones','check')
    search_fields = ['medio']
    fieldsets = (
        ('Datos del Medio', {
            'fields': ('medio',('tipo','genero'),('inicio','inicioyear'),('direccion','sitioweb'),'propietario','fuentepropiedad','grupo','logo'),
        }),
        ('Datos Cobertura -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('cobertura','region','comuna','ciudad'),
        }),
        ('Medio Asociado a -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('asociadoaescrito','asociadoaradio','asociadoacanaltv','asociadoamediodigital'),
        }),
        ('Datos de Rating -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('rating','inforating','fuenterating'),
        }),
        ('Extra -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('telefono','observaciones','anexos','check'),
        }),
        ('Ejecutivos -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('ejecutivouno','ejecutivounocargo','ejecutivounocargofecha'),('ejecutivodos','ejecutivodoscargo','ejecutivodoscargofecha'),('ejecutivotres','ejecutivotrescargo','ejecutivotrescargofecha'),('ejecutivocuatro','ejecutivocuatrocargo','ejecutivocuatrocargofecha'),('ejecutivocinco','ejecutivocincocargo','ejecutivocincocargofecha'),('ejecutivoseis','ejecutivoseiscargo','ejecutivoseiscargofecha'),('ejecutivosiete','ejecutivosietecargo','ejecutivosietecargofecha'),('ejecutivoocho','ejecutivoochocargo','ejecutivoochocargofecha'),('ejecutivonueve','ejecutivonuevecargo','ejecutivonuevecargofecha'),('ejecutivodiez','ejecutivodiezcargo','ejecutivodiezcargofecha')),
        }),
    )
    readonly_fields=('app',)

class MediosDigitalesAdmin(admin.ModelAdmin):
    list_display = ('medio','nativoasociado','genero','inicioyear','visitaspaginasvistas','visitasunicas','director','sitioweb','observaciones','check')
    search_fields = ['medio']
    fieldsets = (
        ('Datos del Medio', {
            'fields': (('medio','sitioweb'),('genero','nativoasociado'),('inicio','inicioyear','pagado_gratuito'),'direccion','propietario','fuentepropiedad','grupo','logo'),
        }),
        ('Datos de Cobertura -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('cobertura','region','comuna','ciudad'),
        }),
        ('Datos de Visitas -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('visitaspaginasvistas','visitasunicas','infovisitas','fuentevisitas'),
        }),
        ('Medio Asociado a -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('asociadoaescrito','asociadoaradio','asociadoacanaltv','asociadoamediodigital'),
        }),
        ('Extra -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': ('telefono','observaciones','anexos','check'),
        }),
        ('Ejecutivos -click para abrir-', {
             'classes': ('grp-collapse grp-closed',),
            'fields': (('ejecutivouno','ejecutivounocargo','ejecutivounocargofecha'),('ejecutivodos','ejecutivodoscargo','ejecutivodoscargofecha'),('ejecutivotres','ejecutivotrescargo','ejecutivotrescargofecha'),('ejecutivocuatro','ejecutivocuatrocargo','ejecutivocuatrocargofecha'),('ejecutivocinco','ejecutivocincocargo','ejecutivocincocargofecha'),('ejecutivoseis','ejecutivoseiscargo','ejecutivoseiscargofecha'),('ejecutivosiete','ejecutivosietecargo','ejecutivosietecargofecha'),('ejecutivoocho','ejecutivoochocargo','ejecutivoochocargofecha'),('ejecutivonueve','ejecutivonuevecargo','ejecutivonuevecargofecha'),('ejecutivodiez','ejecutivodiezcargo','ejecutivodiezcargofecha')),
        }),
    )
    readonly_fields=('app',)

class ListaFuentes(admin.ModelAdmin):
    list_display = ('fuente','linkfuente')
    search_fields = ['fuente']

class ListaGrupos(admin.ModelAdmin):
    list_display = ('grupo','paisorigen')
    search_fields = ['grupo']

class ListaAutores(admin.ModelAdmin):
    list_display = ('autor','datosautor')
    search_fields = ['autor']

class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('documento','tipodocumento','linkdocumento')
    search_fields = ['documento']
    fieldsets = (
        ('Datos de la norma', {
            'fields': ('documento','tipodocumento','descripciondocumento','actores','linkdocumento'),
        }),
    )

class ArticuloAdminForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('autor','fecha','pais','titulo','subtitulo','extracto','cuerpo','imagen_destacada','destacado','posicion')
        widgets = {
           'cuerpo': RedactorEditor(),
        }

class ArticuloAdmin(admin.ModelAdmin):
    form = ArticuloAdminForm

"""
class EscritoResource(resources.ModelResource):
    class Meta:
        model = Escrito

class CanalTVResource(resources.ModelResource):
    class Meta:
        model = CanalTV

class RadioResource(resources.ModelResource):
    class Meta:
        model = Radio

class MedioDigitalResource(resources.ModelResource):
    class Meta:
        model = MedioDigital

class PropietarioResource(resources.ModelResource):
    class Meta:
        model = Propietario

class SociedadResource(resources.ModelResource):
    class Meta:
        model = Sociedad

class GrupoResource(resources.ModelResource):
    class Meta:
        model = Grupo

class RegulacionResource(resources.ModelResource):
    class Meta:
        model = Regulacion

class EscritoAdmin(ImportExportActionModelAdmin):
    resource_class = EscritoResource
    pass

class CanalTVAdmin(ImportExportActionModelAdmin):
    resource_class = CanalTVResource
    pass

class RadioAdmin(ImportExportActionModelAdmin):
    resource_class = RadioResource
    pass

class MedioDigitalAdmin(ImportExportActionModelAdmin):
    resource_class = MedioDigitalResource
    pass

class PropietarioAdmin(ImportExportActionModelAdmin):
    resource_class = PropietarioResource
    pass

class SociedadAdmin(ImportExportActionModelAdmin):
    resource_class = SociedadResource
    pass

class RegulacionAdmin(ImportExportActionModelAdmin):
    resource_class = RegulacionResource
    pass

class GrupoAdmin(ImportExportActionModelAdmin):
    resource_class = GrupoResource
    pass
"""

admin.site.register(Ejecutivo,ListaEjecutivos)
admin.site.register(Empresario,ListaEmpresarios)
admin.site.register(GeneroEscrito)
admin.site.register(Region,ListaRegiones)
admin.site.register(Comuna,ListaComunas)
admin.site.register(Ciudad,ListaCiudades)
admin.site.register(Sector)
admin.site.register(Cargo)
admin.site.register(Periodicidad)
admin.site.register(Propietario,ListaPropietarios)
admin.site.register(TipoSociedad)
admin.site.register(PaisSociedad,ListaPaises)
admin.site.register(Sociedad,ListaSociedades)
admin.site.register(Escrito,MedioEscritoAdmin)
admin.site.register(GeneroRadio)
admin.site.register(Radio,RadiosAdmin)
admin.site.register(GeneroCanalTV)
admin.site.register(CanalTV,CanalesTVAdmin)
admin.site.register(GeneroMedioDigital)
admin.site.register(MedioDigital,MediosDigitalesAdmin)
admin.site.register(Fuente,ListaFuentes)
admin.site.register(Autor,ListaAutores)
admin.site.register(Grupo,ListaGrupos)
admin.site.register(TipoDocumento)
admin.site.register(Regulacion,DocumentosAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Etiqueta)