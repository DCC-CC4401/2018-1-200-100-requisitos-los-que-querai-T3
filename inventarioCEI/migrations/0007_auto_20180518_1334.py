# Generated by Django 2.0.3 on 2018-05-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioCEI', '0006_auto_20180516_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='tipo_objeto',
            field=models.CharField(choices=[('Artículo', 'Artículo'), ('Espacio', 'Espacio')], default='Artículo', max_length=50),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('En préstamo', 'En préstamo'), ('En reparación', 'En resparación'), ('Perdido', 'Perdido')], default='Disponible', max_length=50),
        ),
        migrations.AlterField(
            model_name='espacio',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('En préstamo', 'En préstamo'), ('En reparación', 'En resparación')], default='Disponible', max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado_reserva',
            field=models.CharField(choices=[('Pediente', 'Pendiente'), ('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada')], default='Pendiente', max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='tipo_objeto',
            field=models.CharField(choices=[('Artículo', 'Artículo'), ('Espacio', 'Espacio')], default='Artículo', max_length=50),
        ),
    ]
