from django.shortcuts import render
from .forms import ContactoForm
from django.contrib.auth.decorators import login_required
from apps.email.email import create_mail

def contacto(request):
    context = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Mensaje Enviado!'
        else:
            context['form'] = formulario
            context['mensaje'] = 'El formulario no es valido!'


    return render(request, 'contacto/contacto.html', context)

def EnviarEmail(contacto):
    return create_mail(
        "Se han contactado con nosotros",
        'email.html',
        {
            'nombre':contacto.nombre,
            'correo':contacto.correo,
            'mensaje': contacto.mensaje
        }
    )