# Django Imports
from website.models import HomePage, AboutUsPage, ContactUsPage


class WebsiteService:
    @staticmethod
    def get_home_page():
        return HomePage.objects.first()
   
    @staticmethod
    def get_about_page():
        return AboutUsPage.objects.first()

    @staticmethod 
    def get_contact_page():
        return ContactUsPage.objects.first()