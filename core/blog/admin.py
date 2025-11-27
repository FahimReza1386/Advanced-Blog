# Django Imports 
from django.contrib import admin

# Third-Party Imports
from modeltranslation.admin import TranslationAdmin
# Local Imports
from blog.models.blog import BlogModel, BlogCategoryModel, BlogImageModel

@admin.register(BlogModel)
class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'type', 'status', 'created_at')
    list_filter = ('type', 'status')
    search_fields = ('title', 'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(BlogImageModel)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('blog', 'image', 'created_at')
    list_filter=('blog__title',)
    search_fields = ('blog__title',)