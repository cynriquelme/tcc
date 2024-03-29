# Generated by Django 3.2 on 2022-03-19 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0005_auto_20220319_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(blank=True, default=16, on_delete=django.db.models.deletion.CASCADE, to='registration.person'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='transmitter',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
