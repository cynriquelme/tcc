from django.db import models
#from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import User
from crud.models import SubCategory

class Register(models.Model):
    description = models.CharField(max_length=600, verbose_name="Descripción", unique=True)
    registration_date = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    status = models.BooleanField(verbose_name="Activo", default=True, help_text="Indica si el registro está Activo o Inactivo.")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=0, verbose_name="Sub Categoría")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description

class CodeQR(models.Model):
    generated_code = models.CharField(max_length=200, verbose_name="Código QR", unique=True)
    registre = models.ForeignKey(Register, on_delete=models.CASCADE, default=0, verbose_name="Registro")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Código QR'
        verbose_name_plural = 'Códigos QR'
        ordering = ["-create_date"]

    def __str__(self):
        return self.generated_code

