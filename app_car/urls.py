from django.urls import path
from app_car import views
from app_car.views import HomeView,serviceListView


urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("about/", views.about, name ='about'),
    path("fleet/", views.fleet, name ='fleet'),
    path("gallery/", views.gallery, name ='gallery'),
    path("privacy/", views.privacy, name ='privacy'),
    path("faq/", views.faq, name ='faq'),
     path("price/", views.pricetable, name ='price'),
    path("booking/", views.booking, name='booking'),
    path("services/", serviceListView.as_view(), name ='services'),
    path("contact/", views.contact, name ='contact'),
    path("servicedetails/", views.servicedetails, name ='servicedetails'),
    path('reviews/', views.create_review, name='reviews'),
]