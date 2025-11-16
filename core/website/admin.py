from django.contrib import admin

# Local Imports
from website.models import HomePage, AboutUsPage, ContactUsPage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    def has_add_permission(self, request):
        if HomePage.objects.exists() != True:
            return True 

@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
   
    def has_add_permission(self, request):
        if AboutUsPage.objects.exists() != True:
            return True 

@admin.register(ContactUsPage)
class ContactUsPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    def has_add_permission(self, request):
        if ContactUsPage.objects.exists() != True:
            return True 