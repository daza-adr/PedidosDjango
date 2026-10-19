from django.urls import path

from . import views


urlpatterns = [
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedidos/nuevo/', views.pedido_form, name='pedido_create'),
    path('pedidos/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedidos/<int:pk>/editar/', views.pedido_form, name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', views.pedido_delete, name='pedido_delete'),
]