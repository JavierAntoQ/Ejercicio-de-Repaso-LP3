"""Ejercicio_de_Repaso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('inicio/',views.index, name = "inicio"),
    path('crear_autor/<str:nombre>/<str:apellido>/<str:sexo>/<str:fecha_nac>/<str:pais>',views.crear_autor, name="crear_autor"),
    path('buscar_autor',views.buscar_autor, name="buscar_autor"),
    path('editar_autor/<int:id>',views.editar_autor, name="editar_autor"),
    path('listar_autores', views.listar_autores, name="listar_autores"),
    path('eliminar_autor/<int:id>',views.eliminar_autor, name="eliminar_autor"),
    path('save-autor/',views.save_autor, name="save_autor"),
    path('create-autor/',views.create_autor, name="create_autor"),
]
