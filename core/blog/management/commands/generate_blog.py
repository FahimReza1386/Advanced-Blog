# Django Import
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


# Third-Party Imports
from faker import Faker
from PIL import Image
from io import BytesIO
import requests
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

                    image_url = f"https://picsum.photos/200/200?random={random.randint(1, 1000)}"
                    response = requests.get(image_url)

                    image = Image.open(BytesIO(response.content))

                    image_size = len(response.content)

                    if image_size > 1048576:
                        image = self.resize_image(image)

                    image_file = self.save_image(image)
                    
                    BlogImageModel.objects.create(blog=blog, image=image_file)

        self.stdout.write(self.style.SUCCESS('Successfully generated fake blog data.'))


    def resize_image(self, image):
        image = image.resize((800, 800), Image.ANTIALIAS)
        return image

    def save_image(self, image):
        img_io = BytesIO()
        image.save(img_io, format="JPEG", quality=85)
        img_io.seek(0)
        return ContentFile(img_io.read(), name="image.jpg")