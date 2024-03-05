from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistroForm
from django.urls import reverse_lazy
from .models import Usuario
from apps.noticias.models import Noticia
from apps.productos.models import Producto
from apps.contacto.models import Contacto
from django.contrib.auth.decorators import login_required
# Vista para el inicio de sesión
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_panel') # Redirección a la página de inicio después del inicio de sesión
        else:
            messages.error(request, 'Usuario o contraseña inválido, intente de nuevo')
    
    return render(request, 'usuarios/login.html')

# Vista para el cierre de sesión
def user_logout(request):
    logout(request)
    return redirect('login')


# Vista para el registro de usuarios  /*
"""
class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'
"""
@login_required
def admin_panel(request):
    if request.method == 'POST':
        idContacto = request.POST.get('id')
        contacto = Contacto.objects.get(id = idContacto)
        contacto.visto = True
        contacto.save()
    users = Usuario.objects.all()
    noticias = Noticia.objects.all()
    productos= Producto.objects.all()
    contactos = Contacto.objects.filter(visto = False)
    return render(request, 'usuarios/admin_panel.html', {'users': users,'noticias':noticias,'productos': productos,'contactos':contactos})

