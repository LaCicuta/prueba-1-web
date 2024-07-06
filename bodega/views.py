from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pais, Ciudad, Sexo, Rubro, Empresa, Productos, Usuario
from django.contrib.auth.decorators import login_required
from .forms import PaisForm, CiudadForm, SexoForm, RubroForm, UsuarioForm
from django.contrib import messages

# Create your views here.

def index(request):
    context = {}
    return render(request, 'bodega/index.html', context)

def nosotros(request):
    context = {}
    return render(request, 'bodega/nosotros.html', context)

def registrarse(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        lName = request.POST["lName"]
        email = request.POST["email"]
        pais = request.POST["pais"]
        ciudad = request.POST["ciudad"]
        sexo = request.POST["sexo"]
        phone = request.POST["phone"]
        fNac = request.POST["fNac"]
        nickName = request.POST["nickName"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]

        print("Datos recibidos del formulario:")
        print(f"Rut: {rut}, Nombre: {nombre}, Apellido: {lName}, Email: {email}, País: {pais}, Ciudad: {ciudad}, Sexo: {sexo}, Teléfono: {phone}, Fecha Nacimiento: {fNac}, Nickname: {nickName}, Contraseña: {password}, Dirección: {direccion}")

        objPais = Pais.objects.get(idPais = pais)
        objCiudad = Ciudad.objects.get(idCiudad = ciudad)
        objSexo = Sexo.objects.get(idSexo = sexo)
        objEmpresa = Empresa.objects.get(rolEmpresa = 1)
        obj = Usuario.objects.create(idUsuario=rut,
                                     userName=nombre,
                                     userAp=lName,
                                     userMail=email,
                                     idPais=objPais,
                                     idCiudad=objCiudad,
                                     idSexo=objSexo,
                                     phone=phone,
                                     userNacimiento=fNac,
                                     userMote=nickName,
                                     passwordUsuario=password,
                                     userDireccion=direccion,
                                     rolEmpresa=objEmpresa,
                                     activo = 1)
        print("Objeto Usuario creado:", obj)
        obj.save()
        print("Datos guardados en la base de datos")
        return render(request, 'bodega/index.html')
    
    else:
        ciudades = Ciudad.objects.all()
        paises = Pais.objects.all()
        sexos = Sexo.objects.all()
        context = {'ciudades': ciudades, 'paises': paises, 'sexos': sexos,}
        return render(request, 'bodega/registrarse.html', context)


def inicio(request):
    context = {}
    return render(request, 'bodega/inicio.html', context)

def contactanos(request):
    context = {}
    return render(request, 'bodega/contactanos.html', context)


def inventario(request):
    context = {}
    return render(request, 'bodega/inventario.html', context)

def login(request):
    context = {}
    return render(request, 'registration/login.html', context)  

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
def eliminar_usuario(request, id):
    msj=[]
    error=[]
    usuario = Usuario.objects.all()
    try:
        usuario = Usuario.objects.get(idUsuario=id)
        context={}
        if usuario:
            usuario.delete()
            msj.append('Usuario eliminado correctamente')
            context = {'usuario':usuario, 'msj':msj, 'error':error}
            return render(request, 'inicioAdmin', context)
    except:
        print("Error. Usuario no existe.")
        usuario=Usuario.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'usuario':usuario}
        error.append('No existe el usuario')
        return redirect('inicioAdmin')

