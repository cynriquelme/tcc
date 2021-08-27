from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from crud.models import TypeReport, SubCategory
from django.db import models


class Report(models.Model):
    day  = timezone.now()
    hour = timezone.now()
    #formatedHour = hour.strftime("%Y/%m/%d %H:%M:%S")
    formatedDay  = day.strftime("%Y-%m-%d")
    formatedHour = hour.strftime("%H:%M")
    
    description = models.CharField(max_length=600, verbose_name="Descripción", unique=True)
    found_date = models.DateField(verbose_name="Fecha", default=formatedDay)
    found_time = models.TimeField(verbose_name="Hora", default=formatedHour)
    image = models.ImageField(verbose_name="Imagen", upload_to='reports')
    status = models.BooleanField(verbose_name="Activo", default=True, help_text="Indica si el registro está Activo o Inactivo.")
    type_report = models.ForeignKey(TypeReport, on_delete=models.CASCADE, default=0, verbose_name="Tipo de Reporte")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=0, verbose_name="Sub Categoría")
    coord_latitude = models.CharField(max_length=50)
    coord_length = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ["-create_date"]

    def __str__(self):
        return self.description