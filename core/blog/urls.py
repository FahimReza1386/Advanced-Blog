# Django Imports
from django.urls import path

# Local Imports
from . import views

app_name = 'blog'
urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='blog-list'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
]