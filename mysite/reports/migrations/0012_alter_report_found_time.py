# Generated by Django 3.2 on 2022-03-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_alter_report_found_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='found_time',
            field=models.TimeField(default='11:33', verbose_name='Hora'),
        ),
    ]
