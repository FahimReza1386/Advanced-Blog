# Django Imports
from django.contrib import admin

# Third-Party Imports
from modeltranslation.admin import TranslationAdmin
# Local Imports
from website.models import HomePage, AboutUsPage, ContactUsPage

@admin.register(HomePage)
class HomePageAdmin(TranslationAdmin):
    list_display = ('title',)
    
    def has_add_permission(self, request):
        if HomePage.objects.exists() != True:
            return True 
        
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(AboutUsPage)
class AboutUsPageAdmin(TranslationAdmin):
    list_display = ('title',)
   
    def has_add_permission(self, request):
        if AboutUsPage.objects.exists() != True:
            return True 
        
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(ContactUsPage)
class ContactUsPageAdmin(TranslationAdmin):
    list_display = ('title',)
    
    def has_add_permission(self, request):
        if ContactUsPage.objects.exists() != True:
            return True 
        
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }