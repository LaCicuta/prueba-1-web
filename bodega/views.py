from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'bodega/index.html', context)

def nosotros(request):
    context = {}
    return render(request, 'bodega/nosotros.html', context)

def registrarse(request):
    context = {}
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