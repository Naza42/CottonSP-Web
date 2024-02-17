from django.shortcuts import render, get_object_or_404,redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
@login_required()
def cargar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/cargar_producto.html', {'form': form})