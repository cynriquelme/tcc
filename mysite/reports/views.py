import django
from .models import Report, Coordinate
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django import forms
from crud.models import TypeReport, SubCategory


# Create your views here.
class ReportListView(ListView):
    model = Report

class ReportDetailView(DetailView):
    model = Report

@method_decorator(staff_member_required, name='dispatch')
class ReportCreate(CreateView):
    model = Report
    fields = ['type_report', 'sub_category', 'image', 'description', 'found_date', 'found_time',  'status',]
    success_url = reverse_lazy('reports:reports')

    def get_object(self):
        # recuperar el objeto que se va a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(ReportCreate, self).get_form()
        # Modificar en tiempo real
        form.fields['description'].widget = forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese una descripción'})
        return form