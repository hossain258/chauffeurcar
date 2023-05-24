from django.urls import path
from app_car import views


urlpatterns = [
    path("", views.home, name='home'),
    
]