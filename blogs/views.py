
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


from .blog_generator import BlogGenerator

from .models import Blog
from .forms import BlogUpdateForm

import json

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'blogs/index.html'


class BlogListView(LoginRequiredMixin, ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user).order_by('-created_at')


class BlogDetailView(LoginRequiredMixin, DetailView):
    template_name = 'blogs/blog_detail.html'
    context_object_name = "blog"
    model = Blog
    pk_url_kwarg = 'pk'
    
    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blogs/blog_update.html'
    form_class = BlogUpdateForm

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('blog-list')

@csrf_exempt
@login_required
def get_blog(request):
    if request.method == 'POST':
        requested_data = json.loads(request.body)
        print(1)
        youtube_link = requested_data.get('youtube_link')
        print(2)
        if youtube_link is None:
            return JsonResponse({
                "error": "Youtube link is not valid."
            }, status=400)

        try:
            response = BlogGenerator.generate(youtube_video_link=youtube_link)
            print(3)
            blog = Blog.objects.create(
                user = request.user,
                title = response["title"],
                video_link = youtube_link,
                content = response["content"]
            )
            print(4)
            if response['status'] is False:
                return JsonResponse({
                    "error":True,
                    "message":"Request limit exceeded at OpenAI.",
                    "blog":response["content"]
                }, status=201)
            
            return JsonResponse({
                "error":False,
                "message":"Successfully Generated.",
                "blog": response["content"]
            }, status=201)
        
        except Exception as e:
            print(5)
            return JsonResponse({
                "error":True,
                "message":"Something bad had happend!",
                "blog":""
            }, status=500)
