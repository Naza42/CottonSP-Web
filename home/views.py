from django.shortcuts import render
from apps.contacto.forms import ContactoFormIndex
def home(request):
    formulario = ContactoFormIndex()
    mensaje = ''
    if request.method == "POST":
        formulario = ContactoFormIndex(request.POST)
        print("FORMULARIO")
        if formulario.is_valid():
            mensaje = "Muchas Gracias por ponerte en contacto con nosotros. Intentaremos responder lo mas antes posible"
        
    return render(request, 'home.html',{'form':formulario,'mensaje':mensaje})


def quienes_somos(request):
    return render(request, 'quienes_somos.html')

