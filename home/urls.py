from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('set_language', views.set_language_view,name='set_language'),
    path('cottonAcademy',views.cottonAcademy,name='cottonAcademy')
]