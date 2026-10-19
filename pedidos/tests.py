from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Pedido


class PedidoModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            password='admin123',
            email='admin@example.com',
        )

    def test_pedido_requires_unique_number(self):
        Pedido.objects.create(
            numero_pedido='PED-001',
            cliente='Ana García',
            descripcion='Pedido básico',
            valor_total=50,
            estado='pendiente',
            usuario=self.user,
        )
        pedido = Pedido(
            numero_pedido='PED-001',
            cliente='Luis Pérez',
            descripcion='Otro pedido',
            valor_total=80,
            estado='confirmado',
            usuario=self.user,
        )
        with self.assertRaises(ValidationError):
            pedido.full_clean()

    def test_user_can_register_from_page(self):
        response = self.client.post(
            '/registro/',
            {
                'username': 'nuevo_usuario',
                'password1': 'Admin12345',
                'password2': 'Admin12345',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username='nuevo_usuario').exists())