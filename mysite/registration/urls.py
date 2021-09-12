from django.urls import path
from .views import ProfileUpdate, SignUpView, EmailUpdate, terms_v
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('terms/', views.terms_v, name="terms"),
]