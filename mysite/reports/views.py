import django
from django.http import request
from .models import Report
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django import forms
from crud.models import TypeReport, SubCategory
from django.contrib.auth.models import User
from .forms import ReportForm, ReportUpdate
from django.template import RequestContext


# Create your views here.
class ReportListView(ListView):
    template_name = 'reports/report_list.html­'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        return Report.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['message'] = 'Lista de Reportes'
        return context

class ReportDetailView(DetailView):
    model = Report

def report_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('reports:reports')
    else:
        form = ReportForm()
        print("entro 2")
    return render(request, 'reports/report_form.html', {'form': form})

class ReportUpdate(UpdateView):
    model = Report
    form_class = ReportUpdate
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse_lazy('reports:update', args=[self.object.id]) + '?ok'


class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('reports:reports')