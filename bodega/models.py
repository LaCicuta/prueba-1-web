from django.db import models

# Create your models here.

class Pais(models.Model):
    idPais = models.AutoField(db_column='idPais',primary_key=True)
    nombrePais = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombrePais


class Ciudad(models.Model):
    idCiudad = models.AutoField(db_column='idCiudad',primary_key=True)
    nombreCiudad = models.CharField(max_length=50, blank=False, null=False)
    idPais = models.ForeignKey('Pais', on_delete=models.CASCADE, db_column='idPais')

    def __str__(self):
        return self.nombreCiudad


class Sexo(models.Model):
    idSexo = models.AutoField(db_column='idSexo',primary_key=True)
    detalleSexo = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.detalleSexo


class Rubro(models.Model):
    idRubro = models.AutoField(db_column='idRubro',primary_key=True)
    descRubro = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.descRubro
    

class Empresa(models.Model):
    rolEmpresa = models.CharField(max_length=15,db_column='idEmpresa',primary_key=True)
    nombreEmpresa = models.CharField(max_length=100, blank=False, null=False)
    idRubro = models.ForeignKey('Rubro', on_delete=models.CASCADE, db_column='idRubro')
    descripcion = models.CharField(max_length=1500, blank=False, null=False)

    def __str__(self):
        return self.nombreEmpresa


class Productos(models.Model):
    idProducto = models.IntegerField(db_column='idProducto',primary_key=True)
    rolEmpresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, db_column='idEmpresa')
    nombreProducto = models.CharField(max_length=50, blank=False, null=False)
    descProducto = models.CharField(max_length=500, blank=False, null=False)
    peso = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.nombreProducto


class CodePais(models.Model):
    idCodPais = models.AutoField(db_column='idCodPais',primary_key=True)
    idPais = models.ForeignKey('Pais', on_delete=models.CASCADE, db_column='idPais')
    codigoPhonePais = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.codigoPhonePais
    
class Usuario(models.Model):
    idUsuario = models.IntegerField(db_column='idUsuario',primary_key=True)
    userMote = models.CharField(max_length=50, blank=False, null=False)
    userName = models.CharField(max_length=50, blank=False, null=False)
    userAp = models.CharField(max_length=50, blank=False, null=False)
    userMail = models.CharField(max_length=50, blank=False, null=False)
    idCiudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, db_column='idCiudad')
    idSexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, db_column='idSexo')
    idCodPais = models.ForeignKey('CodePais', on_delete=models.CASCADE, db_column='idCodPais')
    phone = models.CharField(max_length=10, blank=False, null=False)
    userNacimiento = models.DateField(blank=False, null=False)
    userWebPage = models.CharField(max_length=100)
    userDireccion = models.CharField(max_length=100)
    rolEmpresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, db_column='idEmpresa')
    passwordUsuario = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.userName

