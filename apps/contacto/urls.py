from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contacto'

urlpatterns = [
    path('contacto', views.contacto, name='contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
