# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Third-Party Imports
from ckeditor.fields import RichTextField

# Local Imports

class HomePage(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name=_("عنوان")
    )
    
    class Meta:
        verbose_name = _("صفحه خانه")
        verbose_name_plural = _("صفحه خانه")

    def __str__(self):
        return self.title

class AboutUsPage(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("عنوان")
    )
    content = RichTextField(
        verbose_name=_("محتوا")
    )
    
    class Meta:
        verbose_name = _("صفحه درباره ما")
        verbose_name_plural = _("صفحه درباره ما")

    def __str__(self):
        return f"About Us Page {self.id}"
    
class ContactUsPage(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("عنوان")
    )
    email=models.EmailField(
        max_length=200,
        verbose_name=_("ایمیل")
    )
    instagram_link = models.CharField(
        max_length=200,
        verbose_name=_("لینک اینستاگرام")
    )
    facebook_link = models.CharField(
        max_length=200,
        verbose_name=_("لینک فیسبوک")
    )
    linkedin_link = models.CharField(
        max_length=200,
        verbose_name=_("لینک لینکدین")
    )
    twitter_link = models.CharField(
        max_length=200,
        verbose_name=_("لینک توییتر")
    )
    owner_name=models.CharField(
        max_length=200,
        verbose_name=_("نام مدیریت")
    )
    phone_number= models.CharField(
        max_length=11,
        verbose_name=_("شماره تلفن")
    )
    working_hours= models.CharField(
        max_length=200,
        verbose_name=_("ساعات کاری")
    )
    address= models.CharField(
        max_length=300,
        verbose_name=_("آدرس")
    )

    class Meta:
        verbose_name = _("صفحه ارتباط با ما")
        verbose_name_plural = _("صفحه ارتباط با ما")

    def __str__(self):
        return f"Contact Us Page {self.id}"