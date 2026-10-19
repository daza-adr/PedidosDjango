from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from productos.models import Producto

from .forms import PedidoForm
from .models import Pedido


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
    return render(
        request,
        'pedidos/dashboard.html',
        {
            'total_productos': Producto.objects.count(),
            'total_pedidos': Pedido.objects.count(),
            'pendientes': Pedido.objects.filter(estado='pendiente').count(),
        },
    )


@login_required(login_url='login')
def pedido_list(request):
    query = request.GET.get('q', '')
    estado_filtro = request.GET.get('estado', '')
    pedidos = Pedido.objects.all()
    if estado_filtro:
        pedidos = pedidos.filter(estado=estado_filtro)
    if query:
        pedidos = pedidos.filter(cliente__icontains=query)
    pedidos = pedidos.order_by('-fecha_registro')
    return render(
        request,
        'pedidos/pedido_list.html',
        {'pedidos': pedidos, 'query': query, 'estado_filtro': estado_filtro},
    )


@login_required(login_url='login')
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedidos/pedido_detail.html', {'pedido': pedido})


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
    return render(request, 'pedidos/pedido_form.html', {'form': form, 'pedido': pedido})


@login_required(login_url='login')
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado correctamente.')
        return redirect('pedido_list')
    return redirect('pedido_detail', pk=pedido.pk)