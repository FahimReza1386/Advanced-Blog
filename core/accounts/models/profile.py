# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Third-Party Imports
from ckeditor.fields import RichTextField

# Local Imports
from utils.models import DatetimeModel
from accounts.models.user import UserModel

class ProfileModel(DatetimeModel):
    first_name = models.CharField(
        max_length=100,
        verbose_name=_("نام")
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_("نام خانوادگی")
    )
    user = models.OneToOneField(
        UserModel, 
        on_delete=models.CASCADE, 
        related_name='user_profile',
        verbose_name=_("کاربر")
    )
    bio = RichTextField(
        blank=True, 
        null=True,
        verbose_name=_("بیوگرافی")
    )
    profile = models.ImageField(
        upload_to='profile/', 
        default='profile/user.png',
        verbose_name=_("تصویر پروفایل")
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        verbose_name=_("شماره تلفن")
    ) 

    class Meta:
        verbose_name = _('پروفایل')
        verbose_name_plural = _('پروفایل‌ها')
        ordering = ['id']