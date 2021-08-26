from django import forms
from django.forms import models
from django.forms.forms import Form
from .models import Coordinate, Report
from django.contrib.admin import widgets

class DateInput (forms.DateInput):
    input_type = 'date'

class TimeInput (forms.TimeInput):
    input_type = 'time'
    
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['type_report', 'sub_category','description', 'found_date', 'found_time', 'status' ]
        widgets = {
            'description': forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese una descripción'}),
            'found_date': DateInput(attrs = {'class':'form-control mb-2 mt-3 '}),
            'found_time': TimeInput(attrs = {'class':'form-control mb-2 mt-3'}),
            'type_report': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
            'sub_category': forms.Select(attrs={'class':'form-control mb-2 mt-3'}),
            #'image': forms.ClearableFileInput(attrs={'class':'form-control-file mb-2 mt-3'}),
        }

class CoordinateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['c_latitude', 'c_length']
        widgets = {
            #'image': forms.ClearableFileInput(attrs={'class':'form-control-file mb-2 mt-3'}),
        }