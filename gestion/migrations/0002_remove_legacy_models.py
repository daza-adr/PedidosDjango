from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gestion', '0001_initial'),
        ('pedidos', '0001_adopt_gestion_pedido'),
        ('productos', '0001_adopt_gestion_producto'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(name='Pedido'),
                migrations.DeleteModel(name='Producto'),
            ],
        ),
    ]