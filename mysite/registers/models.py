from django.db import models
#from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import User
from crud.models import SubCategory
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from .validators import valid_extension

class Register(models.Model):
    description = models.CharField(max_length=600, verbose_name="Descripción", unique=True)
    qr_code = models.ImageField(verbose_name= "", upload_to='qr_codes',null=False, blank=True,validators=[valid_extension])
    registration_date = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    reported = models.BooleanField(verbose_name="Reportar", default=False, help_text="Indica si el registro ha sido extraviado.")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=0, verbose_name="Sub Categoría")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        ordering = ['-registration_date','-user']

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        data = "http://127.0.0.1:8000/accounts/profile/owner/" + str(self.user.id) + "/"
        qrcode_img = qrcode.make(data)
        canvas = Image.new('RGB', (400, 400), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr-{self.description}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


