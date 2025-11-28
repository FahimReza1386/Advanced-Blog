# Django Import
from django.core.management.base import BaseCommand


# Third-Party Imports
from faker import Faker
import random

# Locale Imports
from blog.models.blog import BlogModel, BlogCategoryModel, BlogImageModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake =Faker(locale="fa_IR")
        categories = BlogCategoryModel.objects.all()
        for _ in range(10):
            blog = BlogModel.objects.create(
                title=fake.word(),
                description=fake.paragraph(nb_sentences=5),
                type=2,
                status=1,
                category=random.choice(categories)
            )
            for _ in range(3):
                BlogImageModel.objects.create(
                    blog=blog,
                    image='blog_images/image.jpg'
                )
        self.stdout.write(self.style.SUCCESS('Successfully generated fake blog data.'))