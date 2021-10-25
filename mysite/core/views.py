from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.template import loader
from reports.models import Report
from crud.models import Category, SubCategory

def home(request):
    reports = Report.objects.all()
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    template = "core/home.html"
    return render(request, template,{"reports":reports, "categories":categories, "sub_categories":sub_categories, "request":request})
