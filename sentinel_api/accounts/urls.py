from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/register/', views.RegistrationView.as_view(), name='register'),
    path('api/profile/', views.UserProfileView.as_view(), name='profile'),
]