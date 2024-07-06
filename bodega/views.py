from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pais, Ciudad, Sexo, Rubro, Empresa, Productos, Usuario, CodePais
from django.contrib.auth.decorators import login_required
from .forms import PaisForm, CiudadForm, SexoForm, RubroForm


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
    pais = Pais.objects.get(id=id)
    pais.delete()
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
    ciudad = Ciudad.objects.get(id=id)
    ciudad.delete()
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
    sexo = Sexo.objects.get(id=id)
    sexo.delete()
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
    rubro = Rubro.objects.get(id=id)
    rubro.delete()
    return redirect('inicioAdmin')
