# Django Imports
from django.core.management.base import BaseCommand

# Third-Party Imports
from faker import Faker

# Locale Imports
from blog.models import BlogCategoryModel

class Command(BaseCommand):
    help = "Gnerate 5 Categories with Faker Packages"
   
    def handle(self, *args, **options):
        faker = Faker(locale="fa_IR")
        
        for _ in range(5):
            title= faker.word()
            BlogCategoryModel.objects.create(
                title=title,
            )
        
        self.stdout.write(self.style.SUCCESS("Successfully to Create The 5 Faker Categories"))
        
        