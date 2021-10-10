from django.urls import path
from . import views
from .views import RegisterDelete, RegisterListView, RegisterDetailView, RegisterUpdate, CodeQRCreate

registers_patterns = ([
    path('', RegisterListView.as_view(), name='registers'),
    path('<int:pk>/<slug:register_slug>/', RegisterDetailView.as_view(), name='register'),
    path('create', views.register_new, name= 'create'),
    path('update/<int:pk>/', RegisterUpdate.as_view(), name= 'update'),
    path('delete/<int:pk>/', RegisterDelete.as_view(), name= 'delete'),
    path('qrcode/', views.generate_qrcode, name='qrcode'),
    path('scanner_qr/', views.scanner_qr, name='scanner_qr'),
], 'registers' )