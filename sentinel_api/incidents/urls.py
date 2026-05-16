from django.urls import path
from . import views

urlpatterns = [
    path('api/incident/', views.IncidentView.as_view(), name='incident'),
    path('api/incident/<int:id>/', views.IncidentDetailView.as_view(), name='incident-detail'),
    
]