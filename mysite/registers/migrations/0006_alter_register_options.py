# Generated by Django 3.2 on 2022-01-20 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0005_register_qr_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register',
            options={'ordering': ['create_date'], 'verbose_name': 'Registro', 'verbose_name_plural': 'Registros'},
        ),
    ]