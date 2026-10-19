from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Producto


class ProductoModelTests(TestCase):
    def test_producto_requires_positive_price(self):
        producto = Producto(
            nombre='Teclado',
            descripcion='Teclado mecánico',
            precio=0,
            cantidad_disponible=5,
        )
        with self.assertRaises(ValidationError):
            producto.full_clean()