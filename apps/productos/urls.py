from django.urls import path
from . import views

urlpatterns = [
    path('cargar/', views.cargar_producto, name='cargar_producto'),
    path('', views.lista_productos, name='lista_productos'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    # Otras URLs aquí...
]
