import django
from .models import Category, Register
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django import forms

# Create your views here.
class RegisterListView(ListView):
    model = Register

class RegisterDetailView(DetailView):
    model = Register

@method_decorator(staff_member_required, name='dispatch')
class RegisterCreate(CreateView):
    model = Register
    fields = ['sub_category', 'description', 'status']
    success_url = reverse_lazy('registers:registers')

    def get_form(self, form_class=None):
        form = super(RegisterCreate, self).get_form()
        # Modificar en tiempo reald
        form.fields['description'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Ingrese una descripción'})
        return form

@method_decorator(staff_member_required, name='dispatch')
class RegisterUpdate(UpdateView):
    model = Register
    fields = ['sub_category', 'description', 'status']
    template_name_suffix = '_update_form'
  
    def get_success_url(self) -> str:
        return reverse_lazy('registers:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class RegisterDelete(DeleteView):
    model = Register
    success_url = reverse_lazy('registers:registers')

    