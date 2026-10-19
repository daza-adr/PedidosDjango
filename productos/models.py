from django.core.exceptions import ValidationError
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'gestion_producto'
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