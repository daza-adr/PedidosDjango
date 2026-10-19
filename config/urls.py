from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from pedidos import views as pedido_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pedido_views.dashboard, name='dashboard'),
    path('registro/', pedido_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', include('productos.urls')),
    path('', include('pedidos.urls')),
]
