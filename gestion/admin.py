from django.contrib import admin

from .models import Pedido, Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'cantidad_disponible', 'fecha_registro']
    search_fields = ['nombre']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['numero_pedido', 'cliente', 'estado', 'valor_total', 'usuario', 'fecha_registro']
    list_filter = ['estado', 'fecha_registro']
    search_fields = ['numero_pedido', 'cliente']
