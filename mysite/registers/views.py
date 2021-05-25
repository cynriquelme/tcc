from django.forms import forms
from .models import Register
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
class RegisterListView(ListView):
    model = Register

class RegisterDetailView(DetailView):
    model = Register

class RegisterCreate(CreateView):
    model = Register
    fields = ['sub_category', 'description', 'status']
    success_url = reverse_lazy('registers:registers')

class RegisterUpdate(UpdateView):
    model = Register
    fields = ['sub_category', 'description', 'status']
    template_name_suffix = '_update_form'
  
    def get_success_url(self) -> str:
        return reverse_lazy('registers:update', args=[self.object.id]) + '?ok'

class RegisterDelete(DeleteView):
    model = Register
    success_url = reverse_lazy('registers:registers')