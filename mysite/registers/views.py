import django
from .models import Register, CodeQR
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django import forms
from six import BytesIO
import qrcode
from .forms import RegisterForm

# Create your views here.
class RegisterListView(ListView):
    model = Register

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

@method_decorator(staff_member_required, name='dispatch')
class CodeQRCreate(CreateView):
    model = CodeQR
    fields = ['generated_code', 'register']
    success_url = reverse_lazy('registers:registers')

    def get_object(self):
        # recuperar el objeto que se va a editar
        return self.request.user

def generate_qrcode(request):
    user = request.user.id
    print(user)
    data = "http://127.0.0.1:8000/accounts/profile/owner/" + str(user) + "/" 
    img = qrcode.make(data)

    buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    return response
    

    

