# Third-Party Imports
from modeltranslation.translator import register, TranslationOptions

# Locale Imports
from website.models import HomePage, AboutUsPage, ContactUsPage

@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
@register(AboutUsPage)
class AboutUsPageTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'content',
    )
@register(ContactUsPage)
class ContactUsPageTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'owner_name',
        'address',
    )