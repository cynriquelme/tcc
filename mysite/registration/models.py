from django.db import models
from django.contrib.auth.models import User
from crud.models import TypeDocument, Sexe, City, Departament, Country

# Create your models here.
class Person(models.Model):
    type_document = models.ForeignKey(TypeDocument, on_delete=models.CASCADE, default=0, verbose_name="Tipo de Documento")
    number_document = models.CharField(max_length=50, verbose_name="Número de Documento")
    names = models.CharField(max_length=200, verbose_name="Nombres")
    last_names = models.CharField(max_length=200, verbose_name="Apellidos")
    birthday = models.DateField(verbose_name="Fecha de Nacimiento")
    phone = models.CharField(max_length=50, verbose_name="Teléfono")
    email = models.EmailField(max_length=200, verbose_name="Email")
    sexe = models.ForeignKey(Sexe, on_delete=models.CASCADE, default=0, verbose_name="Sexo")
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0, verbose_name="Ciudad")
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default=0, verbose_name="Departamento")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=0, verbose_name="País")
    direction = models.CharField(max_length=200, verbose_name="Domicilio")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ["-create_date"]

    def __str__(self):
        return self.names + ' ' + self.last_names

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Persona", default=4)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, blank=True)