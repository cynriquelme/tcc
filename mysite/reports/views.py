import django
from django.http import request
from .models import Report
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django import forms
from crud.models import TypeReport, SubCategory
from django.contrib.auth.models import User
from .forms import ReportForm
from django.template import RequestContext


# Create your views here.
class ReportListView(ListView):
    model = Report

class ReportDetailView(DetailView):
    model = Report

def report_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print("entro")
            return redirect('reports:reports')
    else:
        form = ReportForm()
        print("entro 2")
    return render(request, 'reports/report_form.html', {'form': form})