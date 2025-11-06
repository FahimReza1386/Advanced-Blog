# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Local Imports
from utils.models import DatetimeModel
from accounts.managers.user_manager import UserManager

class UserModel(DatetimeModel, AbstractBaseUser, PermissionsMixin):

    class UserTypeModel(models.IntegerChoices):
        customer= 1,_("مشتری")
        admin= 2,_("ادمین")
        superuser= 3,_("کاربر ارشد")

    email = models.EmailField(
        unique=True,
        verbose_name=_("ایمیل")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("فعال شده")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("پرسنل")
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name=_("تایید شده")
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_("کاربر ارشد")
    )
    type = models.IntegerField(
        choices=UserTypeModel.choices, 
        default=UserTypeModel.customer.value,
        verbose_name=_("نوع")
    )

    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'

    objects = UserManager() 

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')
        ordering = ['id']
