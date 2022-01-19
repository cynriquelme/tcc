from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.template import loader
from reports.models import Report
from crud.models import Category, SubCategory
from django.core.paginator import Paginator
from django.shortcuts import render
from .filters import ReportF


def home(request):
    reports = Report.objects.all()
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    reports_count = reports.count()
    reports_filter = ReportF(request.GET, queryset=reports)
    reports = reports_filter.qs
    template = "core/home.html"
    paginator = Paginator(reports, 20) #Se visualizará 20 reportes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template,{"reports":reports, "categories":categories, "sub_categories":sub_categories,"reports_count":reports_count, "reports_filter":reports_filter, 
    "request":request, 'page_obj': page_obj})
