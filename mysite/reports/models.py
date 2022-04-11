from email.policy import default
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from crud.models import TypeReport, SubCategory
from registers.models import Register
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

class Report(models.Model):
    day  = timezone.now()
    hour = timezone.now()
    formatedDay  = day.strftime("%Y-%m-%d")
    formatedHour = hour.strftime("%H:%M")
    description = models.CharField(max_length=600, verbose_name="Descripción", unique=True)
    found_date = models.DateField(verbose_name="Fecha", default=formatedDay)
    found_time = models.TimeField(verbose_name="Hora", default=formatedHour)
    image = models.ImageField(verbose_name="Imagen", upload_to='reports', default=None)
    status = models.BooleanField(verbose_name="Activo", default=True, help_text="Indica si el registro está Activo o Inactivo.")
    type_report = models.ForeignKey(TypeReport, on_delete=models.CASCADE, default=0, verbose_name="Tipo de Reporte")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=0, verbose_name="Sub Categoría")
    reward = EncryptedCharField(max_length=100, verbose_name="Recompensa", blank=True)
    coord_latitude = models.CharField(verbose_name="Coordenada Latitud", max_length=50)
    coord_length = models.CharField(verbose_name="Coordenada Longitud",max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    register  = models.CharField(verbose_name="Registro", blank=True, max_length=50)
    

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['-create_date']

    def __str__(self):
        return self.description

    