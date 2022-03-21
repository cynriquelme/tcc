from cProfile import label
from email.policy import default
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from crud.models import Sexe, City, Departament, Country
from django.conf import settings

def custom_uploap_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre", help_text="Ingrese su Nombre")
    last_name = models.CharField(max_length=200, verbose_name="Apellido", help_text="Ingrese su Apellido")
    birthday = models.DateField(default=0,verbose_name="Fecha de Nacimiento", help_text="Seleccione su Fecha de Nacimiento")
    phone = models.CharField(max_length=50, verbose_name="Teléfono", help_text="Ingrese su Teléfono")
    sexe = models.ForeignKey(Sexe, on_delete=models.CASCADE, default=0, verbose_name="Sexo", help_text="Seleccione su Sexo")
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0, verbose_name="Ciudad", help_text="Seleccione su Ciudad")
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, default=0, verbose_name="Departamento", help_text="Seleccione su Departamento")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=0, verbose_name="País", help_text="Seleccione su País")
    direction = models.CharField(max_length=200, verbose_name="Dirección", help_text="Ingrese su Dirección")

class Profile(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_uploap_to, null=True, blank=True)

@receiver(post_save, sender=User)
def ensure_profile_exits(sender, instance, **kwargs):
    if kwargs.get('created', False): 
        person_id = Person.objects.latest('id')
        Profile.objects.get_or_create(user=instance, person=person_id)
        print("Se acaba de crear un usuario y su perfil enlazado")

class Notification(models.Model):
    message = models.TextField(verbose_name="Mensaje")
    transmitter = models.CharField(max_length=200, verbose_name="Emisor")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Receptor")
    read = models.BooleanField(verbose_name="Leído", default=False, help_text="Indica si el mensaje ha sido leído o no.")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")