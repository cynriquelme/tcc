# Generated by Django 3.2 on 2022-03-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20220318_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='found_date',
            field=models.DateField(default='2022-03-19', verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='report',
            name='found_time',
            field=models.TimeField(default='10:10', verbose_name='Hora'),
        ),
    ]
