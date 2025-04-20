
from django.contrib import admin
from django.urls import path, include
from miapp import views


urlpatterns = [
    path('eliminar/<int:pk>', views.eliminar_socio, name='eliminar_socio'),
    path('editar/<int:pk>', views.editar_socio, name='editar_socio'),
    path('crear/', views.crear_socio, name='crear_socio'),
    path('listar_socios/', views.listar_socios, name='listar_socios'),
    path('index/', views.inicio, name='index'),
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
    path('accounts/', include('django.contrib.auth.urls')),
]
