# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Third-Party Imports
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
# Local Imports
from utils.models import DatetimeModel

class BlogModel(DatetimeModel):

    class BlogTypeModel(models.IntegerChoices):
        premium = 1, _("ویژه"),
        general = 2, _("عادی"),
    
    class BlogStatusModel(models.IntegerChoices):
        publish = 1, _("نمایش"),
        draft = 2, _("عدم نمایش"),
    
    title = models.CharField(
        max_length=255,
        verbose_name=_("عنوان")
    )
    description = RichTextField(
        verbose_name=_("جزئیات")
    )
    status = models.IntegerField(
        choices=BlogStatusModel.choices,
        default=BlogStatusModel.publish.value,
        verbose_name=_("وضعیت")
    )
    type = models.IntegerField(
        choices=BlogTypeModel.choices,
        default=BlogTypeModel.premium.value,
        verbose_name=_("نوع")
    )
    
    class Meta:
        verbose_name = _("بلاگ")
        verbose_name_plural = _("بلاگ ها")
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class BlogCategoryModel(DatetimeModel, MPTTModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("اسم")
    ),
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("والد")
    ),

    class Meta:
        verbose_name = _("دسته بندی بلاگ")
        verbose_name_plural = _("دسته بندی های بلاگ")
        ordering = ['-id']

    def __str__(self):
        return self.title