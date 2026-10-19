from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_registro']

    def clean(self):
        super().clean()
        if not self.nombre or len(self.nombre.strip()) < 3:
            raise ValidationError({'nombre': 'El nombre es obligatorio y debe tener al menos 3 caracteres.'})
        if self.precio is None or self.precio <= 0:
            raise ValidationError({'precio': 'El precio debe ser un número mayor que cero.'})
        if self.cantidad_disponible is None or self.cantidad_disponible < 0:
            raise ValidationError({'cantidad_disponible': 'La cantidad disponible no puede ser negativa.'})
        if self.descripcion and len(self.descripcion.strip()) > 500:
            raise ValidationError({'descripcion': 'La descripción no puede superar 500 caracteres.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_pedido = models.CharField(max_length=50, unique=True)
    cliente = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=500)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')

    class Meta:
        ordering = ['-fecha_registro']

    def clean(self):
        super().clean()
        if not self.numero_pedido or not self.numero_pedido.strip():
            raise ValidationError({'numero_pedido': 'El número del pedido es obligatorio.'})
        if not self.cliente or len(self.cliente.strip()) < 2:
            raise ValidationError({'cliente': 'El nombre del cliente es obligatorio.'})
        if not self.descripcion or not self.descripcion.strip():
            raise ValidationError({'descripcion': 'La descripción del pedido es obligatoria.'})
        if self.valor_total is None or self.valor_total <= 0:
            raise ValidationError({'valor_total': 'El valor total debe ser un número mayor que cero.'})
        if self.estado not in dict(self.ESTADO_CHOICES):
            raise ValidationError({'estado': 'El estado seleccionado no es válido.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.numero_pedido} - {self.cliente}'
