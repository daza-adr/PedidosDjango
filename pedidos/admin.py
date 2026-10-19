from django.contrib import admin

from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['numero_pedido', 'cliente', 'estado', 'valor_total', 'usuario', 'fecha_registro']
    list_filter = ['estado', 'fecha_registro']
    search_fields = ['numero_pedido', 'cliente']