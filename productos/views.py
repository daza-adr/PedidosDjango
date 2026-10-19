from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


@login_required(login_url='login')
def producto_list(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query).order_by('-fecha_registro')
    return render(request, 'productos/producto_list.html', {'productos': productos, 'query': query})


@login_required(login_url='login')
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/producto_detail.html', {'producto': producto})


@login_required(login_url='login')
def producto_form(request, pk=None):
    producto = get_object_or_404(Producto, pk=pk) if pk else None
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto guardado correctamente.')
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_form.html', {'form': form, 'producto': producto})


@login_required(login_url='login')
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('producto_list')
    return redirect('producto_detail', pk=producto.pk)