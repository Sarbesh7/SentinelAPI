from django.urls import path
from . import views

urlpatterns = [
    
    path('api/citizen-dashboard/', views.CitizenDashboard.as_view(), name='citizen-dashboard'),
    
    path('api/responder-dashboard/', views.ResponderDashboard.as_view(), name='responder-dashboard'),
    
    path('api/admin-dashboard/', views.AdminDashboard.as_view(), name='admin-dashboard'),
    
    path('api/admin/users/', views.AdminUserManagement.as_view(), name='admin-users-list'),
    
    path('api/admin/users/<int:user_id>/', views.AdminUserManagement.as_view(), name='admin-user-update'),
]