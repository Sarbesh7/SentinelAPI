from django.urls import path
from . import views

urlpatterns = [
    path('api/notifications/', views.NotificationView.as_view(), name='notifications'),
    path('api/notifications/<int:id>/', views.NotificationDetailView.as_view(), name='notification-detail'),
]
