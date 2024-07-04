#from django.conf.urls import url
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

]