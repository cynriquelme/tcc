from email import message
from re import template
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import decorators
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm, PersonForm, NotificationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django import forms
from .models import Notification, Profile, Person
from django.shortcuts import redirect, render, HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.db.models import Count


# Create your views here.
class SignUpView(CreateView):
    model = Person
    form_class = UserCreationFormWithEmail
    second_form_class = PersonForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self). get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request,*args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            person = form.save(commit=False)
            person.user = form2.save()
            person.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2= form2))

    def get_success_url(self):
        return reverse_lazy('login') + '?success'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar la contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar el objeto que se va a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo'})
        return form

def terms_v(request):
    return render(request,'registration/terms.html')

def profile_author(request,user):
    try:
        profile=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return HttpResponse('El Propietario Ingresado no existe. ')

    return render(
        request,
        'registration/profile_author.html',
        context={'profile':profile}
    )

def profile_owner_v(request,user):
    try:
        profile=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return HttpResponse('El Propietario Ingresado no existe. ')
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.receiver = profile.user
            post.save()
            print("entro notification")
            return HttpResponseRedirect('' + '?success') 
    else:
        form = NotificationForm()
        print("entro notification 2")

    return render(
        request,
        'registration/profile_owner.html',
        context={'profile':profile, 'form': form}
    )

class NotificationListView(ListView):
    template_name= 'registration/notification_list.html'
    paginate_by = 15
    
    def get_queryset(self, *args, **kwargs):
        return Notification.objects.filter(receiver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Notificationes'
        return context

class NotificationUpdate(UpdateView):
    model = Notification
    fields = ['read']
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse_lazy('notification') + '?ok'