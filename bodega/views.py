from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.hashers import make_password
from login.forms import *
from django.contrib.auth.views import LoginView
from login.forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'login/login.html'

# Create your views here.
    
def index(request):
    form = LoginForm()
    return render(request, 'bodega/index.html', {'form': form})

def nosotros(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'bodega/nosotros.html', context)


def registrarse(request):
    form = LoginForm()
    if request.method == "POST":
        userForm = RegistroUsuario(request.POST)
        if userForm.is_valid():
            cd = userForm.cleaned_data
            newUser = Usuario(
                idUsuario=cd['idUsuario'],
                userName=cd['userName'],
                userAp=cd['userAp'],
                userMail=cd['userMail'],
                idPais_id=cd['idPais'],
                idCiudad_id=cd['idCiudad'],
                idSexo_id=cd['idSexo'],
                phone=cd['phone'],
                userNacimiento=cd['userNacimiento'],
                userMote=cd['userMote'],
                userDireccion=cd['userDireccion'],
                rolEmpresa=cd['rolEmpresa'],  # Asignar el valor de rolEmpresa como instancia
                activo=1,
                passwordUsuario=make_password(cd['password'])
            )
            newUser.save()
            return redirect('inicio')  # Redirigir a la página de inicio después de un registro exitoso
        else:
            # Construir una cadena con los errores del formulario
            error_messages = "\n".join([f"{field}: {error}" for field, errors in userForm.errors.items() for error in errors])
            return HttpResponse(f'Formulario Inválido:\n{error_messages}')
    else:
        userForm = RegistroUsuario()
    return render(request, 'bodega/registrarse.html', {'userForm': userForm, 'form': form})


def inicio(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        try:
            usuario = Usuario.objects.get(idUsuario=usuario_id)
        except Usuario.DoesNotExist:
            return HttpResponse('Usuario no encontrado en la base de datos')
        context = {'usuario': usuario}
        return render(request, 'bodega/inicio.html', context)
    else:
        return redirect('login')
    
    
def contactanos(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'bodega/contactanos.html', context)


def inventario(request):
    context = {}
    return render(request, 'bodega/inventario.html', context)
