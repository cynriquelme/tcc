# Generated by Django 3.2 on 2021-08-16 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(upload_to='reports', verbose_name='Imagen'),
        ),
    ]