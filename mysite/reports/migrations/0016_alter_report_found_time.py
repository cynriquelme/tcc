# Generated by Django 3.2 on 2022-03-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0015_alter_report_found_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='found_time',
            field=models.TimeField(default='15:34', verbose_name='Hora'),
        ),
    ]
