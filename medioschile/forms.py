from django.forms import ModelForm
from django.forms import forms
from medioschile.models import *

class EscritoForm(ModelForm):
    class Meta:
        model = Escrito
        fields = '__all__'

class CanalTVForm(ModelForm):
    class Meta:
        model = CanalTV
        fields = '__all__'

class RadioForm(ModelForm):
    class Meta:
        model = Radio
        fields = '__all__'

class MedioDigitalForm(ModelForm):
    class Meta:
        model = MedioDigital
        fields = '__all__'

'''
class ContactoForm(forms.Form):
	su_nombre = forms.CharField(label='Nombre', max_length=200)
	asunto = forms.CharField(label='Asunto', max_length=100)
	mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)
	email = forms.EmailField()
'''