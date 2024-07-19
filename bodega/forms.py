from django import forms
from django.forms import ModelForm
from .models import *


class RegistroUsuario(forms.Form):
    idUsuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut', 'id': 'rut'}))
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'name'}))
    userAp = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'id': 'lName'}))
    userMail = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email'}))
    idPais = forms.ChoiceField(
        choices=[(pais.idPais, pais.nombrePais) for pais in Pais.objects.all()],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'pais'}))
    idCiudad = forms.ChoiceField(
        choices=[(ciudad.idCiudad, ciudad.nombreCiudad) for ciudad in Ciudad.objects.all()],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'ciudad'}))
    idSexo = forms.ChoiceField(
        choices=[(sexo.idSexo, sexo.detalleSexo) for sexo in Sexo.objects.all()],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'sexo'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'id': 'phone'}))
    userNacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Nacimiento', 'id': 'fNac'}))
    userMote = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname', 'id': 'nickName'}))
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'id': 'password'}))
    password2 = forms.CharField(
        label='Repita Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita Contraseña', 'id': 'password2'}))
    userDireccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'id': 'direccion'}))
    activo = 1
    rolEmpresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Usuario
        fields = ['idUsuario', 'userName', 'userAp', 'userMail', 'idPais', 'idCiudad', 'idSexo', 'userNacimiento', 'phone', 'userMote', 'password', 'password2', 'userDireccion', 'rolEmpresa', 'activo']

    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['rolEmpresa'].initial = Empresa.objects.get(pk=1)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    
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

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
