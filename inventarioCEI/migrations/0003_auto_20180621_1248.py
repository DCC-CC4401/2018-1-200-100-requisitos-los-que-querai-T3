# Generated by Django 2.0.5 on 2018-06-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioCEI', '0002_auto_20180605_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('En préstamo', 'En préstamo'), ('En reparación', 'En reparación')], default='Disponible', max_length=50),
        ),
    ]