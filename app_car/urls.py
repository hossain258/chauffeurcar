from django.urls import path
from app_car import views
from app_car.views import HomeView,serviceListView


urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("about/", views.about, name ='about'),
    path("fleet/", views.fleet, name ='fleet'),
    path("faq/", views.faq, name ='faq'),
    path("booking/", views.booking, name='booking'),
    path("services/", serviceListView.as_view(), name ='services'),
    path("contact/", views.contact, name ='contact'),
]