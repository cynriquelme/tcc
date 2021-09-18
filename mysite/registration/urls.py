from django.urls import path
from .views import ProfileUpdate, SignUpView, EmailUpdate
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('terms/', views.terms_v, name="terms"),
    path('profile/owner/<int:pk>/', views.profile_owner_v, name="profile_owner"),
]