# Generated by Django 3.2 on 2022-03-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20220317_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='found_time',
            field=models.TimeField(default='21:15', verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reward',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Recompensa'),
        ),
    ]
