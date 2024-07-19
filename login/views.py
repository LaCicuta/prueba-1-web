from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from bodega.views import *  # Importar todas las vistas desde bodega.views
from bodega.models import Usuario  # Importar el modelo Usuario
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()

def logout_view(request):
    logout(request)
    return redirect('index')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # Guardar solo el id del usuario en la sesión
                    return redirect('inicioAdmin')
                else:
                    return HttpResponse('Usuario no activo')
            else:
                # Verificar si el usuario existe en el modelo Usuario por correo o userMote
                try:
                    usuario = Usuario.objects.get(userMail=cd['username'])
                    request.session['usuario_id'] = user.idUsuario
                except Usuario.DoesNotExist:
                    try:
                        usuario = Usuario.objects.get(userMote=cd['username'])
                    except Usuario.DoesNotExist:
                        return HttpResponse('Usuario no existe o es incorrecto')
                
                # Verificar la contraseña
                if usuario.passwordUsuario == (cd['password']):
                    request.session['usuario_id'] = usuario.idUsuario
                    return redirect('inicio')
                else:
                    return HttpResponse('Contraseña incorrecta')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


@login_required
def inicioAdmin(request):
    pais = Pais.objects.all()
    ciudad = Ciudad.objects.all()
    sexo = Sexo.objects.all()
    rubro = Rubro.objects.all()
    usuario = Usuario.objects.all()
    context={'pais':pais, 'ciudad':ciudad, 'sexo':sexo, 'rubro':rubro, 'usuario':usuario}
    return render(request, 'administracion/admin-inicio.html', context) 

@login_required
def paisAdd(request):
    print("estoy en controlador paisAdd...")
    context = {}
    
    if request.method == "POST":
        print("controlador es un post...")
        form = PaisForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()
            form = PaisForm()
            context = {'mensaje': "Ok, datos grabados...", 'form': form}
            return redirect('inicioAdmin')
    else:
        form = PaisForm()
        context = {'form': form}
        return render(request, 'administracion/agregar_datos.html', context)

@login_required    
def modificar_pais(request, id):
    try:
        pais = Pais.objects.get(idPais=id)
        context={}
        if pais:
            print("Edit encontró el Pais...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = PaisForm(request.POST, instance=pais)
                form.save()
                print("Bien, datos actualizados...")
                mensaje = "País actualizado"
                context = {'pais': pais, 'form': form, 'mensaje': mensaje}
                return redirect('inicioAdmin')
            else:
                print("Edit, NO es un POST")
                form = PaisForm(instance=pais)
                context = {'pais': pais, 'form': form}
                return render(request, 'administracion/editar_datos.html', context)
    except:
        print("Error, id no existe...")
        pais = Pais.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'pais': pais}
        return redirect('inicioAdmin')


@login_required
def eliminar_pais(request, id):
    msj=[]
    error=[]
    pais = Pais.objects.all()
    try:
        pais = Pais.objects.get(idPais=id)
        context={}
        if pais:
            pais.delete()
            messages.success(request, 'Pais eliminado correctamente')
            msj.append('Pais eliminado correctamente')
            context = {'pais':pais, 'msj':msj, 'error':error}
            return redirect('inicioAdmin')
    except:
        print("Error. Pais no existe.")
        messages.error(request, 'Error, id no existe')
        pais=Pais.objects.all()
        error.append('No existe el pais')
        return redirect('inicioAdmin')

@login_required    
def ciudadAdd(request):
    print("estoy en controlador ciudadAdd...")
    context = {}
    
    if request.method == "POST":
        print("controlador es un post...")
        form = CiudadForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()
            form = CiudadForm()
            context = {'mensaje': "Ok, datos grabados...", 'form': form}
            return redirect('inicioAdmin')
    else:
        form = CiudadForm()
        context = {'form': form}
        return render(request, 'administracion/agregar_datos.html', context)

@login_required       
def modificar_ciudad(request, id):
    try:
        ciudad = Ciudad.objects.get(idCiudad=id)
        context={}
        if ciudad:
            print("Edit encontró la Ciudad...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = CiudadForm(request.POST, instance=ciudad)
                form.save()
                print("Bien, datos actualizados...")
                mensaje = "Ciudad actualizada"
                print(mensaje)
                context = {'ciudad': ciudad, 'form': form, 'mensaje': mensaje}
                return redirect('inicioAdmin')
            else:
                print("Edit, NO es un POST")
                form = CiudadForm(instance=ciudad)
                context = {'ciudad': ciudad, 'form': form}
                return render(request, 'administracion/editar_datos.html', context)
    except:
        print("Error, id no existe...")
        ciudad = Ciudad.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'ciudad': ciudad}
        return render(request, 'administracion/editar_datos.html', context)


@login_required
def eliminar_ciudad(request, id):
    msj=[]
    error=[]
    ciudad = Ciudad.objects.all()
    try:
        ciudad = Ciudad.objects.get(idCiudad=id)
        context={}
        if ciudad:
            ciudad.delete()
            msj.append('Ciudad eliminada correctamente')
            context = {'ciudad':ciudad, 'msj':msj, 'error':error}
            return render(request, 'inicioAdmin', context)
    except:
        print("Error. Ciudad no existe.")
        ciudad=Ciudad.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'ciudad':ciudad}
        error.append('No existe la ciudad')
        return redirect('inicioAdmin')

@login_required    
def sexoAdd(request):
    print("estoy en controlador sexoAdd...")
    context = {}
    
    if request.method == "POST":
        print("controlador es un post...")
        form = SexoForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()
            form = SexoForm()
            context = {'mensaje': "Ok, datos grabados...", 'form': form}
            return redirect('inicioAdmin')
    else:
        form = SexoForm()
        context = {'form': form}
        return render(request, 'administracion/agregar_datos.html', context)

@login_required    
def modificar_sexo(request, id):
    try:
        sexo = Sexo.objects.get(idSexo=id)
        context={}
        if sexo:
            print("Edit encontró el Sexo...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = SexoForm(request.POST, instance=sexo)
                form.save()
                print("Bien, datos actualizados...")
                mensaje = "Género actualizado"
                context = {'sexo': sexo, 'form': form, 'mensaje': mensaje}
                return redirect('inicioAdmin')
            else:
                print("Edit, NO es un POST")
                form = SexoForm(instance=sexo)
                context = {'sexo': sexo, 'form': form}
                return render(request, 'administracion/editar_datos.html', context)
    except:
        print("Error, id no existe...")
        sexo = Sexo.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'sexo': sexo}
        return redirect('inicioAdmin')


@login_required
def eliminar_sexo(request, id):
    msj=[]
    error=[]
    sexo = Sexo.objects.all()
    try:
        sexo = Sexo.objects.get(idSexo=id)
        context={}
        if sexo:
            sexo.delete()
            msj.append('Sexo eliminado correctamente')
            context = {'sexo':sexo, 'msj':msj, 'error':error}
            return render(request, 'inicioAdmin', context)
    except:
        print("Error. Sexo no existe.")
        sexo=Sexo.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'sexo':sexo}
        error.append('No existe el sexo')
        return redirect('inicioAdmin')

@login_required
def rubroAdd(request):
    print("estoy en controlador agregar_rubro...")
    context = {}
    
    if request.method == "POST":
        print("controlador es un post...")
        form = RubroForm(request.POST)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()
            form = RubroForm()
            context = {'mensaje': "Ok, datos grabados...", 'form': form}
            return redirect('inicioAdmin')
    else:
        form = RubroForm()
        context = {'form': form}
        return render(request, 'administracion/agregar_datos.html', context)
@login_required
def modificar_rubro(request, id):
    try:
        rubro = Rubro.objects.get(idRubro=id)
        context={}
        if rubro:
            print("Edit encontró el Rubro...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = RubroForm(request.POST, instance=rubro)
                if form.is_valid():
                    form.save()
                    print("Bien, datos actualizados...")
                    mensaje = "Rubro actualizado"
                    context = {'rubro': rubro, 'form': form, 'mensaje': mensaje}
                    return redirect('inicioAdmin')
            else:
                print("Edit, NO es un POST")
                form = RubroForm(instance=rubro)
                context = {'rubro': rubro, 'form': form}
                return render(request, 'administracion/editar_datos.html', context)
    except:
        print("Error, id no existe...")
        rubro = Rubro.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'rubro': rubro}
        return redirect('inicioAdmin')

@login_required
def eliminar_rubro(request, id):
    msj=[]
    error=[]
    rubro = Rubro.objects.all()
    try:
        rubro = Rubro.objects.get(idRubro=id)
        context={}
        if rubro:
            rubro.delete()
            msj.append('Rubro eliminado correctamente')
            context = {'rubro':rubro, 'msj':msj, 'error':error}
            return render(request, 'inicioAdmin', context)
    except:
        print("Error. Rubro no existe.")
        rubro=Rubro.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'rubro':rubro}
        error.append('No existe el rubro')
        return redirect('inicioAdmin')

@login_required    
def modificar_usuario(request, id):
    try:
        usuario = Usuario.objects.get(idUsuario=id)
        context={}
        if usuario:
            print("Edit encontró el Usuario...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = UsuarioForm(request.POST, instance=usuario)
                form.save()
                print("Bien, datos actualizados...")
                mensaje = "Usuario actualizado"
                context = {'usuario': usuario, 'form': form, 'mensaje': mensaje}
                return redirect('inicioAdmin')
            else:
                print("Edit, NO es un POST")
                form = UsuarioForm(instance=usuario)
                context = {'usuario': usuario, 'form': form}
                return render(request, 'administracion/editar_datos.html', context)
    except:
        print("Error, id no existe...")
        usuario = Usuario.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'usuario': usuario}
        return redirect('inicioAdmin')  
      
@login_required
def desactivar_usuario(request, id):
    msj=[]
    error=[]
    usuario = Usuario.objects.all()
    try:
        usuario = Usuario.objects.get(idUsuario=id)
        context={}
        if usuario:
            usuario.activo = 0
            usuario.save() 
            msj.append('Usuario Deshabilitado correctamente')
            context = {'usuario':usuario, 'msj':msj, 'error':error}
            return render(request, 'inicioAdmin', context)
    except:
        print("Error. Usuario no existe.")
        usuario=Usuario.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'usuario':usuario}
        error.append('No existe el usuario')
        return redirect('inicioAdmin')
 
@login_required   
def activar_usuario(request, id):
    msj=[]
    error=[]
    usuario = Usuario.objects.all()
    try:
        usuario = Usuario.objects.get(idUsuario=id)
        context={}
        if usuario:
            usuario.activo = 1
            usuario.save() 
            msj.append('Usuario Habilitado correctamente')
            context = {'usuario':usuario, 'msj':msj, 'error':error}
            return render(request, 'inicioAdmin', context)
    except:
        print("Error. Usuario no existe.")
        usuario=Usuario.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'usuario':usuario}
        error.append('No existe el usuario')
        return redirect('inicioAdmin')
