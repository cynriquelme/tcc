from django.urls import path
from .views import NotificationListView, NotificationUpdate, ProfileUpdate, SignUpView, EmailUpdate
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('terms/', views.terms_v, name="terms"),
    path('profile/owner/<int:user>/', views.profile_owner_v, name="profile_owner"),
    path('profile/author/<int:user>/', views.profile_author, name="profile_author"),
    path('notification/', NotificationListView.as_view(), name='notification'),
    path('notification/update/<int:pk>/', NotificationUpdate.as_view(), name='notification_update'),
]