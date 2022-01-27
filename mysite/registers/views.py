from os import name
import django
from django.contrib.admin.views import decorators
from .models import Register
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django import forms
from six import BytesIO
from .forms import QrForm, RegisterForm
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
from flask import Flask, render_template, request

# Create your views here.
class RegisterListView(ListView):
    template_name= 'registers/register_list.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        return Register.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Registros'

        return context

class RegisterDetailView(DetailView):
    model = Register


def register_new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print("entro register")
            return redirect('registers:registers')
    else:
        form = RegisterForm()
        print("entro 2 register")
    return render(request, 'registers/register_form.html', {'form': form})
    

class RegisterUpdate(UpdateView):
    model = Register
    fields = ['sub_category', 'description', 'status']
    template_name_suffix = '_update_form'
    
    def get_form(self, form_class=None):
        form = super(RegisterUpdate, self).get_form()
        # Modificar en tiempo reald
        form.fields['description'].widget = forms.TextInput(attrs={'class':'form-control mb-2 mt-3', 'placeholder':'Ingrese una descripción'})
        return form

    def get_success_url(self) -> str:
        return reverse_lazy('registers:update', args=[self.object.id]) + '?ok'


class RegisterDelete(DeleteView):
    model = Register
    success_url = reverse_lazy('registers:registers')

def index(request):
    return HttpResponse('ok')
    
def scanner_qr(request):
    if request.method == 'POST':
        formulario = QrForm(request.POST, request.FILES)
        if formulario.is_valid():
            ruta_qr = request.FILES.get('qr_code')
            d = decode(Image.open(ruta_qr))
            print("The total number of elements in the list: ", len(d))
            if (len(d)>0):
                read_qr = d[0].data.decode("ascii")
                result = ""
            else:
                read_qr = ""
                result = "La imagen no puede ser escaneada. Verifique que sea un Código QR."
            return render(request,"registers/scanner_qr_form.html", {'form': formulario, 'read_qr': read_qr,'result': result})
    else:
        formulario = QrForm()
    return render(request, "registers/scanner_qr_form.html",{'form': formulario})


