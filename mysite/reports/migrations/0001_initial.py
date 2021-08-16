# Generated by Django 3.2 on 2021-08-16 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registers', '0004_alter_register_sub_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, unique=True, verbose_name='Descripción')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Tipo de Reporte',
                'verbose_name_plural': 'Tipos de Reportes',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600, unique=True, verbose_name='Descripción')),
                ('found_date', models.DateField(verbose_name='Fecha Encontrada')),
                ('found_time', models.TimeField(verbose_name='Hora Encontrada')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Imagen')),
                ('status', models.BooleanField(default=True, help_text='Indica si el registro está Activo o Inactivo.', verbose_name='Activo')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('sub_category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registers.subcategory', verbose_name='Sub Categoría')),
                ('type_report', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='reports.typereport', verbose_name='Tipo de Reporte')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_latitude', models.FloatField(verbose_name='Latitud')),
                ('c_length', models.FloatField(verbose_name='Longitud')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('report', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='reports.report', verbose_name='Reporte')),
            ],
            options={
                'verbose_name': 'Coordenada',
                'verbose_name_plural': 'Coordenadas',
                'ordering': ['-create_date'],
            },
        ),
    ]
