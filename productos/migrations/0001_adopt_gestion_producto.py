from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name='Producto',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('nombre', models.CharField(max_length=120)),
                        ('descripcion', models.TextField(max_length=500)),
                        ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                        ('cantidad_disponible', models.PositiveIntegerField()),
                        ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                    ],
                    options={
                        'db_table': 'gestion_producto',
                        'ordering': ['-fecha_registro'],
                    },
                ),
            ],
        ),
    ]