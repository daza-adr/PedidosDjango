from django import forms

from .models import Pedido, Producto


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


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'cliente', 'descripcion', 'valor_total', 'estado']
        widgets = {
            'numero_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_numero_pedido(self):
        numero = self.cleaned_data.get('numero_pedido', '').strip()
        if not numero:
            raise forms.ValidationError('El número del pedido es obligatorio.')
        return numero

    def clean_cliente(self):
        cliente = self.cleaned_data.get('cliente', '').strip()
        if not cliente:
            raise forms.ValidationError('El nombre del cliente es obligatorio.')
        return cliente

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion', '').strip()
        if not descripcion:
            raise forms.ValidationError('La descripción del pedido es obligatoria.')
        return descripcion

    def clean_valor_total(self):
        valor_total = self.cleaned_data.get('valor_total')
        if valor_total is not None and valor_total <= 0:
            raise forms.ValidationError('El valor total debe ser mayor que cero.')
        return valor_total
