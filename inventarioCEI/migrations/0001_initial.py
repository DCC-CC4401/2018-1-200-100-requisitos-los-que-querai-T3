

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='../img/articulos')),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('En préstamo', 'En préstamo'), ('En reparación', 'En reparación'), ('Perdido', 'Perdido')], default='Disponible', max_length=50)),
                ('lista_tags', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='../img/espacios')),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('En préstamo', 'En préstamo'), ('En reparación', 'En reparación')], default='Disponible', max_length=50)),
                ('capacidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_ini_prestamo', models.DateTimeField()),
                ('fh_fin_prestamo', models.DateTimeField()),
                ('estado_prestamo', models.CharField(choices=[('Vigente', 'Vigente'), ('Caducado', 'Caducado'), ('Perdido', 'Perdido')], default='Vigente', max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'inventarioCEI'), ('model', 'articulo')), models.Q(('app_label', 'inventarioCEI'), ('model', 'espacio')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('mail', models.EmailField(max_length=150, unique=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('hab', models.CharField(choices=[('Habilitado', 'Habilitado'), ('Inhabilitado', 'Inhabilitado')], default='Habilitado', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_reserva', models.DateTimeField()),
                ('fh_ini_reserva', models.DateTimeField()),
                ('fh_fin_reserva', models.DateTimeField()),
                ('estado_reserva', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada')], default='Pendiente', max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'inventarioCEI'), ('model', 'articulo')), models.Q(('app_label', 'inventarioCEI'), ('model', 'espacio')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventarioCEI.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventarioCEI.Profile'),
        ),
    ]
