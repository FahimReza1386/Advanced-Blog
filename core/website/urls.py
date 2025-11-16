# Django Imports
from django.urls import path

# Local Imports
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about-us/', views.AboutUsPageView.as_view(), name='about-us'),
    path('contact-us/', views.ContactUsPageView.as_view(), name='contact-us'),
]