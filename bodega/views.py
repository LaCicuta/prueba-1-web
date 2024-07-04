from django.shortcuts import render
from .models import Pais, Ciudad, Sexo, Rubro, Empresa, Productos, Usuario, CodePais


# Create your views here.

def index(request):
    context = {}
    return render(request, 'bodega/index.html', context)

def nosotros(request):
    context = {}
    return render(request, 'bodega/nosotros.html', context)

def registrarse(request):
    ciudades = Ciudad.objects.all()
    paises = Pais.objects.all()
    codeFonoPaises = CodePais.objects.all()
    sexos = Sexo.objects.all()
    context = {'ciudades':ciudades, 'paises':paises, 'sexos':sexos,'codeFonoPaises':codeFonoPaises}
    return render(request, 'bodega/registrarse.html', context)

def contactanos(request):
    context = {}
    return render(request, 'bodega/contactanos.html', context)

def inicio(request):
    context = {}
    return render(request, 'bodega/inicio.html', context)

def inventario(request):
    context = {}
    return render(request, 'bodega/inventario.html', context)

