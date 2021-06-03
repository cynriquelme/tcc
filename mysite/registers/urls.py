from django.urls import path
from . import views
from .views import RegisterDelete, RegisterListView, RegisterDetailView, RegisterCreate, RegisterUpdate

registers_patterns = ([
    path('', RegisterListView.as_view(), name='registers'),
    path('<int:pk>/<slug:register_slug>/', RegisterDetailView.as_view(), name='register'),
    path('create', RegisterCreate.as_view(), name= 'create'),
    path('update/<int:pk>/', RegisterUpdate.as_view(), name= 'update'),
    path('delete/<int:pk>/', RegisterDelete.as_view(), name= 'delete'),
    path('qrcode/', views.generate_qrcode)
], 'registers' )