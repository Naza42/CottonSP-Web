from django.shortcuts import render, get_object_or_404,redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    beneficios = producto.resumen_2.split('-')
    return render(request, 'productos/detalle_producto.html', {'producto': producto,'beneficios':beneficios})
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

#-------------------------------BUSCADOR----------------------------------------------------------

#def search(request):
#    return render(request, 'buscador.html')

#def postSearchView(request):
#    queryset = request.GET.get({% blocktrans %} buscar {% endblocktrans %})

#    resultados = {}
#    categorias = Categoria.objects.all()
#    resultados['categorias'] = categorias

#    if queryset:
#        user = NewUser.objects.filter(username = queryset)
#        resultados['posts'] = Post.objects.filter(
#            Q(title__icontains = queryset) |
#            Q(user__in = user)
#        ).distinct()

#    return render(request,'buscador.html', resultados)

#def postCategoryView(request):

#    categoria_id = request.GET.get('filtro', None)

#    resultados = {}
#    categorias = Categoria.objects.all()
#    resultados['categorias'] = categorias

#    if categoria_id:
#        posteos = Post.objects.filter(categoria_id = categoria_id)
#        resultados['posts'] = posteos 

#    return render(request,'post/postCategory.html', resultados)