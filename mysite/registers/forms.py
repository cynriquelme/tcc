from django import forms
from django.forms import models
from django.forms.forms import Form
from .models import Register
from django.contrib.admin import widgets

    
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['sub_category','description', 'status']
        widgets = {
            'description': forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese una descripción'}),
            'sub_category': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)