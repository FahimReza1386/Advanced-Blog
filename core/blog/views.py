# Django Imports
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Third-Party Imports

# Local Imports
from blog.services.blog_services import BlogService
from blog.models import BlogModel

class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model= BlogModel

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['blogs'] = BlogService.get_all_blogs()
        context['images'] = BlogService.get_blog_images()
        return context  
    
class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model= BlogModel

    def dispatch(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.type == BlogModel.BlogTypeModel.premium.value:
            if request.user.is_authenticated:
                return blog
            else:
                messages.error(
                    request,
                    _("مشتری گرامی برای دیدن پست های ویژه باید اشتراک های فهیم وب را تهیه نمیایید .")
                )
                return redirect(reverse_lazy('blog:blog-list'))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        queryset = BlogService.get_detail_blog(self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['images'] = BlogService.get_blog_images()
        return context