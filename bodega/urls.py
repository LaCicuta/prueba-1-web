from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('inicio', views.inicio, name='inicio'),
    path('inventario', views.inventario, name='inventario'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('inicioAdmin', views.inicioAdmin, name='inicioAdmin'),
    path('paisAdd', views.paisAdd, name='paisAdd'),
    path('sexoAdd', views.sexoAdd, name='sexoAdd'),
    path('ciudadAdd', views.ciudadAdd, name='ciudadAdd'),
    path('rubroAdd', views.rubroAdd, name='rubroAdd'),    path('modificar_pais/<int:id>', views.modificar_pais, name='modificar_pais'),
    path('eliminar_pais/<int:id>', views.eliminar_pais, name='eliminar_pais'),
    path('modificar_ciudad/<int:id>', views.modificar_ciudad, name='modificar_ciudad'),
    path('eliminar_ciudad/<int:id>', views.eliminar_ciudad, name='eliminar_ciudad'),   
    path('modificar_sexo/<int:id>', views.modificar_sexo, name='modificar_sexo'),
    path('eliminar_sexo/<int:id>', views.eliminar_sexo, name='eliminar_sexo'),
    path('modificar_rubro/<int:id>', views.modificar_rubro, name='modificar_rubro'),
    path('eliminar_rubro/<int:id>', views.eliminar_rubro, name='eliminar_rubro'),
    path('modificar_usuario/<int:id>', views.modificar_usuario, name='modificar_usuario'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),]