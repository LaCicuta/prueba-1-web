from django.contrib import admin
from .models import Pais, Ciudad, Sexo, Rubro, Empresa, Productos, Usuario

# Register your models here.
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Sexo)
admin.site.register(Rubro)
admin.site.register(Empresa)
admin.site.register(Productos)
admin.site.register(Usuario)

