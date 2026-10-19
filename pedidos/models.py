from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


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
        db_table = 'gestion_pedido'
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