# Generated by Django 3.2 on 2022-01-31 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='departament',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='number_document',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sexe',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='type_document',
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('birthday', models.DateField(default=0, verbose_name='Fecha de Nacimiento')),
                ('phone', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('direction', models.CharField(max_length=200, verbose_name='Domicilio')),
                ('city', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='crud.city', verbose_name='Ciudad')),
                ('country', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='crud.country', verbose_name='País')),
                ('departament', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='crud.departament', verbose_name='Departamento')),
                ('sexe', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='crud.sexe', verbose_name='Sexo')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='person',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.person', verbose_name='Persona'),
        ),
    ]