from django import forms
from .models import Usuario, Pais, Ciudad, Rubro, Sexo

from django.forms import ModelForm

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

class RubroForm(ModelForm):
    class Meta:
        model = Rubro
        fields = '__all__'

class SexoForm(ModelForm):
    class Meta:
        model = Sexo
        fields = '__all__'



