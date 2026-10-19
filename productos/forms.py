from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describa el producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio

    def clean_cantidad_disponible(self):
        cantidad = self.cleaned_data.get('cantidad_disponible')
        if cantidad is not None and cantidad < 0:
            raise forms.ValidationError('La cantidad disponible no puede ser negativa.')
        return cantidad