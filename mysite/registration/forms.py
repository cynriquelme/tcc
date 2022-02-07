from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crud.models import *
from django.contrib.auth.models import User
from .models import Profile, Person
from django.forms import fields, models, widgets

class DateInput (forms.DateInput):
    input_type = 'date'
    
class TimeInput (forms.TimeInput):
    input_type = 'time'

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ingresado ya existe, vuelva a intentar con otro.")
        return email

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El correo ingresado ya existe, vuelva a intentar con otro.")
        return email

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'birthday','phone', 'sexe','country','departament','city','direction']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese su Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese su Apellido'}),        
            'birthday': DateInput(attrs = {'class':'form-control mb-2 mt-3','placeholder':'Seleccione su Fecha de Nacimiento'}),
            'phone': forms.NumberInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese su Teléfono'}),
            'country': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
            'departament': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
            'city': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
            'sexe': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
            'direction': forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese su Dirección'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),        
        }