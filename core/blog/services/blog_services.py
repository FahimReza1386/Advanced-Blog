# Django Imports
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
# Locale Imports
from blog.models import BlogModel, BlogImageModel

class BlogService:
    @staticmethod
    def get_all_blogs():
        return BlogModel.objects.filter(status=BlogModel.BlogStatusModel.publish.value)

    @staticmethod
    def get_blog_images():
        return BlogImageModel.objects.all()
    
    @staticmethod
    def is_authenticated(request):
        if request.user.is_authenticated:
            return True
        return False
    
    @staticmethod
    def get_detail_blog(blog_id):
        blog= get_object_or_404(
            BlogModel,
            id=blog_id,
            status=BlogModel.BlogStatusModel.publish.value
        )
        return blog