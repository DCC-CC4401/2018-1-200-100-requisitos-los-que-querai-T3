# Generated by Django 2.0.3 on 2018-06-04 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioCEI', '0014_auto_20180604_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'inventarioCEI'), ('model', 'Articulo')), models.Q(('app_label', 'inventarioCEI'), ('model', 'Espacio')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'inventarioCEI'), ('model', 'Articulo')), models.Q(('app_label', 'inventarioCEI'), ('model', 'Espacio')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]