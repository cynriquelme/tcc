from calendar import month
from re import template
from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.template import loader
from reports.models import Report
from registration.models import Notification
from crud.models import Category, SubCategory
from django.core.paginator import Paginator
from django.shortcuts import render
from .filters import ReportF
from datetime import datetime
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class DashboardView(TemplateView):
    template_name = 'core/home.html'
    def get_report_found_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for  m in range(1, 13):
                report = Report.objects.filter(found_date__year=year, found_date__month=m, type_report_id=1).count()
                data.append(report)
        except:
            pass
        return data
    
    def get_report_lost_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for  m in range(1, 13):
                report = Report.objects.filter(found_date__year=year, found_date__month=m, type_report_id=2).count()
                data.append(report)
        except:
            pass
        return data

    def get_report_for_category(self):
        data = []
        try:
            year = datetime.now().year
            month = datetime.now().month
            for i in SubCategory.objects.all():
                report = Report.objects.filter(found_date__year=year, found_date__month=month, sub_category_id=i.id).count()
                data.append({
                    'name': i.description,
                    'y': report,
                })
        except:
            pass
        return data   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['report_found_year_month'] = self.get_report_found_year_month
        context['report_lost_year_month'] = self.get_report_lost_year_month
        context['report_for_category'] = self.get_report_for_category
        return context

def extra_context(request):
    if request.user.is_authenticated:
        count_notification = Notification.objects.filter(receiver=request.user,read=False).count()
    else:
        count_notification = None
    return {'count_notification': count_notification }

def search(request):
    reports = Report.objects.all()
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    reports_count = reports.count()
    reports_filter = ReportF(request.GET, queryset=reports)
    reports = reports_filter.qs
    template = "core/search.html"
    paginator = Paginator(reports, 9) #Se visualizará 20 reportes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template,{"reports":reports, "categories":categories, "sub_categories":sub_categories,"reports_count":reports_count, "reports_filter":reports_filter, 
    "request":request, 'page_obj': page_obj})


