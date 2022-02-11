import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

class TypeReport(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Tipo de Reporte'
        verbose_name_plural = 'Tipos de Reportes'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description


class Departament(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description 


class City(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description

    
class Country(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    nacionality = models.CharField(max_length=200, verbose_name="Nacionalidad", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ["-create_date"]

    def __str__(self):
        return (self.description)


class Sexe(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description


class Category(models.Model):
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description

    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0, verbose_name="Categoría")
    description = models.CharField(max_length=200, verbose_name="Descripción", unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Sub Categoria'
        verbose_name_plural = 'Sub Categorias'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description

