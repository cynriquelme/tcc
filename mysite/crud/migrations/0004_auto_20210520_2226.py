# Generated by Django 3.2 on 2021-05-21 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210520_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='found_time',
            field=models.TimeField(verbose_name='Hora Encontrada'),
        ),
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Imagen'),
        ),
    ]
