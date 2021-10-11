from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.template import loader
from reports.models import Report

def home(request):
    reports = Report.objects.all()
    template = loader.get_template('core/home.html')
    return HttpResponse(template.render({'reports': reports}, request))