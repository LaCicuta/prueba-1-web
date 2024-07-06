from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pais, Ciudad, Sexo, Rubro, Empresa, Productos, Usuario, CodePais
from django.contrib.auth.decorators import login_required
from .forms import PaisForm, CiudadForm, SexoForm, RubroForm
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
        objCodePais = CodePais.objects.get(idPais = pais)
        objEmpresa = Empresa.objects.get(rolEmpresa = 1)
        obj = Usuario.objects.create(idUsuario=rut,
                                     userName=nombre,
                                     userAp=lName,
                                     userMail=email,
                                     idPais=objPais,
                                     idCiudad=objCiudad,
                                     idSexo=objSexo,
                                     idCodPais = objCodePais,
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
        codeFonoPaises = CodePais.objects.all()
        sexos = Sexo.objects.all()
        context = {'ciudades': ciudades, 'paises': paises, 'sexos': sexos, 'codeFonoPaises': codeFonoPaises}
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
    context={'pais':pais, 'ciudad':ciudad, 'sexo':sexo, 'rubro':rubro}
    return render(request, 'administracion/admin-inicio.html', context) 

@login_required
def modificar_pais(request, id):
    pais = Pais.objects.get(id=id)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            return redirect('inicioAdmin')
    else:
        form = PaisForm(instance=pais)
    return render(request, 'administracion/modificar_pais.html', {'form': form})

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
        msj="Error, id no existe"
        context={'msj':msj, 'pais':pais}
        error.append('No existe el pais')
        return redirect('inicioAdmin')

@login_required
def modificar_ciudad(request, id):
    ciudad = Ciudad.objects.get(id=id)
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            return redirect('inicioAdmin')
    else:
        form = CiudadForm(instance=ciudad)
    return render(request, 'administracion/modificar_ciudad.html', {'form': form})

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
            messages.success(request, 'Ciudad eliminado correctamente')
            msj.append('Ciudad eliminada correctamente')
            context = {'ciudad':ciudad, 'msj':msj, 'error':error}
            return redirect('inicioAdmin')
    except:
        print("Error. Ciudad no existe.")
        ciudad=Ciudad.objects.all()
        msj="Error, id no existe"
        messages.error(request, 'Error, id no existe')
        context={'msj':msj, 'ciudad':ciudad}
        error.append('No existe la ciudad')
        return redirect('inicioAdmin')

@login_required
def modificar_sexo(request, id):
    sexo = Sexo.objects.get(id=id)
    if request.method == 'POST':
        form = SexoForm(request.POST, instance=sexo)
        if form.is_valid():
            form.save()
            return redirect('inicioAdmin')
    else:
        form = SexoForm(instance=sexo)
    return render(request, 'administracion/modificar_sexo.html', {'form': form})

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
            messages.success(request, 'Sexo eliminado correctamente')
            context = {'sexo':sexo, 'msj':msj, 'error':error}
            return redirect('inicioAdmin')
    except:
        print("Error. Sexo no existe.")
        sexo=Sexo.objects.all()
        msj="Error, id no existe"
        messages.error(request, 'Error, id no existe')
        context={'msj':msj, 'sexo':sexo}
        error.append('No existe el sexo')
        return redirect('inicioAdmin')

@login_required
def modificar_rubro(request, id):
    rubro = Rubro.objects.get(id=id)
    if request.method == 'POST':
        form = RubroForm(request.POST, instance=rubro)
        if form.is_valid():
            form.save()
            return redirect('inicioAdmin')
    else:
        form = RubroForm(instance=rubro)
    return render(request, 'administracion/modificar_rubro.html', {'form': form})

@login_required
def eliminar_rubro(request, id):
    msj=[]
    error=[]
    rubro = Rubro.objects.all()
    try:
        rubro = Rubro.objects.get(id=id)
        context={}
        if rubro:
            rubro.delete()
            messages.success(request, 'Rubro eliminado correctamente')
            msj.append('Rubro eliminado correctamente')
            context = {'rubro':rubro, 'msj':msj, 'error':error}
            return redirect('inicioAdmin')
    except:
        print("Error. Rubro no existe.")
        messages.error(request, 'Error, id no existe')
        rubro=Rubro.objects.all()
        msj="Error, id no existe"
        context={'msj':msj, 'rubro':rubro}
        error.append('No existe el rubro')
        return redirect('inicioAdmin')