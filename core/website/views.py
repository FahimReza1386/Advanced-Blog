# Django Imports
from django.shortcuts import render
from django.views.generic import TemplateView
# Third-Party Imports

# Local Imports
from website.services.website_service import WebsiteService


class HomePageView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = WebsiteService.get_home_page()
        context['contact'] = WebsiteService.get_contact_page()
        return context
    
class AboutUsPageView(TemplateView):
    template_name = "website/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = WebsiteService.get_about_page()
        context['contact'] = WebsiteService.get_contact_page()
        return context
    
class ContactUsPageView(TemplateView):
    template_name = "website/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = WebsiteService.get_contact_page()
        return context 