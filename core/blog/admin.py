# Django Imports 
from django.contrib import admin

# Local Imports
from blog.models.blog import BlogModel, BlogCategoryModel

@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status', 'created_at')
    list_filter = ('type', 'status')
    search_fields = ('title', 'description')

@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'created_at')
    search_fields = ('title',)