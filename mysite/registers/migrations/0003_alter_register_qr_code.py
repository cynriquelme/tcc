# Generated by Django 3.2 on 2022-01-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_auto_20220120_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='qr_code',
            field=models.ImageField(upload_to='qr_codes'),
        ),
    ]