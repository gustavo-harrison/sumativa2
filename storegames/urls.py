"""
URL configuration for storegames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
    path('index', views.inicio, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.formulario, name='formulario'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('ns/', views.ns, name='ns'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('perfil/', views.perfil, name='perfil'),
    path('ps4/', views.ps4, name='ps4'),
    path('ps5/', views.ps5, name='ps5'),
    path('xb360/', views.xb360, name='xb360'),
    path('xbxs/', views.xbxs, name='xbxs'),
    path('admin/', admin.site.urls),
]
