# Generated by Django 3.2 on 2022-03-19 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20220319_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='transmitter',
        ),
    ]
