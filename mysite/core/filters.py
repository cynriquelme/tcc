from unicodedata import category
from django.forms import TextInput
import django_filters 
from django_filters import DateFilter, CharFilter
from crud.models import Category, SubCategory

from reports.models import Report

class ReportF(django_filters.FilterSet):
    star_date = DateFilter(label="Fecha Desde",field_name="found_date", lookup_expr='gte')
    end_date = DateFilter(label="Fecha Hasta",field_name="found_date", lookup_expr='lte')
    description = CharFilter(label="Descripción",field_name="description", lookup_expr='icontains')
    class Meta:
        model = Report
        fields = ['type_report', 'sub_category', 'description']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.form.fields['type_report'].widget.attrs = {'class':'form-control mb-1'} 
        self.form.fields['sub_category'].widget.attrs = {'class':'form-control mb-1'} 
        self.form.fields['description'].widget.attrs = {'class':'form-control mb-1','placeholder':'Escriba una palabra clave'} 
        self.form.fields['star_date'].widget.attrs = {'class':'form-control mb-1','placeholder':'dd/mm/yyyy'} 
        self.form.fields['end_date'].widget.attrs = {'class':'form-control mb-2','placeholder':'dd/mm/yyyy'} 
        self.request_data = args[0].dict()    
