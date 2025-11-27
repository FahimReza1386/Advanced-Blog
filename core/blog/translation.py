# Third-Party Imports
from modeltranslation.translator import register, TranslationOptions

# Locale Imports
from blog.models.blog import BlogModel, BlogCategoryModel



@register(BlogModel)
class BlogModelTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )

@register(BlogCategoryModel)
class BlogCategoryModelTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
