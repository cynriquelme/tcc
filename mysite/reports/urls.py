from django.urls import path
from . import views
from .views import ReportListView, ReportDetailView, report_new, ReportDelete, ReportUpdate

reports_patterns = ([
    path('', ReportListView.as_view(), name='reports'),
    path('<int:pk>/<slug:Report_slug>/', ReportDetailView.as_view(), name='report'),
    path('create', report_new, name= 'create'),
    path('update/<int:pk>/', ReportUpdate.as_view(), name= 'update'),
    path('delete/<int:pk>/', ReportDelete.as_view(), name= 'delete'),
], 'reports' )
