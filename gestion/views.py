from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PedidoForm, ProductoForm
from .models import Pedido, Producto


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada correctamente.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    productos = Producto.objects.count()
    pedidos = Pedido.objects.count()
    pendientes = Pedido.objects.filter(estado='pendiente').count()
    return render(
        request,
        'gestion/dashboard.html',
        {'total_productos': productos, 'total_pedidos': pedidos, 'pendientes': pendientes},
    )


@login_required(login_url='login')
def producto_list(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query).order_by('-fecha_registro')
    return render(request, 'gestion/producto_list.html', {'productos': productos, 'query': query})


@login_required(login_url='login')
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'gestion/producto_detail.html', {'producto': producto})


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
    return render(request, 'gestion/producto_form.html', {'form': form, 'producto': producto})


@login_required(login_url='login')
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('producto_list')
    return redirect('producto_detail', pk=producto.pk)


@login_required(login_url='login')
def pedido_list(request):
    query = request.GET.get('q', '')
    estado_filtro = request.GET.get('estado', '')

    pedidos = Pedido.objects.all()

    if estado_filtro:
        pedidos = pedidos.filter(estado=estado_filtro)
    elif query:
        pedidos = pedidos.filter(cliente__icontains=query)
    else:
        pedidos = pedidos.filter(cliente__icontains=query)

    pedidos = pedidos.order_by('-fecha_registro')
    return render(request, 'gestion/pedido_list.html', {'pedidos': pedidos, 'query': query, 'estado_filtro': estado_filtro})


@login_required(login_url='login')
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'gestion/pedido_detail.html', {'pedido': pedido})


@login_required(login_url='login')
def pedido_form(request, pk=None):
    pedido = get_object_or_404(Pedido, pk=pk) if pk else None
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido_guardado = form.save(commit=False)
            if pedido_guardado.usuario_id is None:
                pedido_guardado.usuario = request.user
            pedido_guardado.save()
            messages.success(request, 'Pedido guardado correctamente.')
            return redirect('pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'gestion/pedido_form.html', {'form': form, 'pedido': pedido})


@login_required(login_url='login')
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado correctamente.')
        return redirect('pedido_list')
    return redirect('pedido_detail', pk=pedido.pk)
