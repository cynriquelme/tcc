# Generated by Django 3.2 on 2021-06-15 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20210607_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(help_text='Fecha de Nacimiento', verbose_name='Fecha de Nacimiento'),
        ),
    ]
