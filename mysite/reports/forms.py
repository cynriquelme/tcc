from django import forms
from .models import Report
from django.contrib.admin import widgets

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['description', 'found_date', 'found_time', 'status', 'type_report', 'sub_category']
        widgets = {
            'description': forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese una descripción'}),
            #'bio': forms.Textarea(attrs={'class':'form-control mt-3','rows':3, 'placeholder':'Biografía'}),
            #'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

        def __init__(self, *args, **kwargs):
            super(ReportForm, self).__init__(*args, **kwargs)
            self.fields['found_date'].widget.attrs['readonly'] = True  
            self.fields['found_time'].widget.attrs['readonly'] = True  