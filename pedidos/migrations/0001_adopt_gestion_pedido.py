import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name='Pedido',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('numero_pedido', models.CharField(max_length=50, unique=True)),
                        ('cliente', models.CharField(max_length=150)),
                        ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                        ('descripcion', models.TextField(max_length=500)),
                        ('valor_total', models.DecimalField(decimal_places=2, max_digits=12)),
                        ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20)),
                        ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
                    ],
                    options={
                        'db_table': 'gestion_pedido',
                        'ordering': ['-fecha_registro'],
                    },
                ),
            ],
        ),
    ]