"""Mapeval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('inicio',views.inicio),
    path('carrito',views.carrito),
    path('formulario',views.formulario),
    path("verFormulario",views.verFormulario),
    path('registroCliente', views.registroCliente),
    path('registroEmpleado',views.registroEmpleado),
    path('iniciarSesion',views.iniciarSesion),
    path('cerrarSesion',views.cerrarSesion),
    path('ingresoProducto',views.ingresoProducto),
    path('productosIngresados',views.verProductosIngresados),
    path('productos',views.productos),
    path('eliminarProducto/<id>/',views.eliminar_producto, name="eliminarProducto"),
    path('detalleProducto/<nombre>',views.Detalles, name="detalleProductos"),
    path('verUsuarios',views.verUsuarios),
    path('eliminar_cliente/<rut>',views.eliminar_cliente, name="eliminar_cliente"),
    path('eliminar_empleado/<rut>',views.eliminar_empleado, name="eliminar_empleado"),
    path('modificarProducto/<id>',views.modificarProducto,name="modificarProducto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
