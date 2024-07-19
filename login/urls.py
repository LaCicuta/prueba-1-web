from django.urls import path
from . import views
from .views import logout_view

urlpatterns =[
    path('', views.user_login, name='login'),
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
    path('modificar_usuario/<slug:id>', views.modificar_usuario, name='modificar_usuario'),
    path('desactivar_usuario/<slug:id>', views.desactivar_usuario, name='desactivar_usuario'),
    path('activar_usuario/<slug:id>', views.activar_usuario, name='activar_usuario'),
    path('logout/', logout_view, name='logout'),
]