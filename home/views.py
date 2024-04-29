from django.shortcuts import render
from apps.contacto.forms import ContactoFormIndex
from django.views.i18n import set_language
from apps.contacto.views import EnviarEmail

def home(request):
    direccion = 'home.html'
    
    formulario = ContactoFormIndex()
    mensaje = ''
    if request.method == "POST":
        formulario = ContactoFormIndex(request.POST)
        if formulario.is_valid():
            mensaje = "Muchas Gracias por ponerte en contacto con nosotros. Intentaremos responder lo mas antes posible"
            form = formulario.save(commit=False)
            try:
                email = EnviarEmail(form)
                if not email.send():
                    form.save()
            except:
                form.save()
            formulario = ContactoFormIndex()

                
    return render(request, direccion,{'form':formulario,'mensaje':mensaje})


def quienes_somos(request):
    direccion = 'quienes_somos.html'
    return render(request, direccion)


    
def cottonAcademy(request):
    return render(request,'cottonAcademy.html')

from django.http import HttpResponseRedirect
from django.utils.translation import activate

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            response = HttpResponseRedirect('/')
            response.set_cookie('django_language', language)
            activate(language)
            return response
    return HttpResponseRedirect('/')