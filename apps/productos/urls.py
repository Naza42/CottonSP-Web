from django.urls import path
from . import views

urlpatterns = [
    path('cargar/', views.cargar_producto, name='cargar_producto'),
    path('', views.lista_productos, name='lista_productos'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
     path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'), 
    # Otras URLs aquí...
]
