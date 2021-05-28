import django
from django.forms import forms
from .models import Register
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

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