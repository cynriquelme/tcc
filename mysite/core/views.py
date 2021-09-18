from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from reports.models import Report

def home(request):
    return render(request, "core/home.html")

class ReportListView(ListView):
    model = Report

