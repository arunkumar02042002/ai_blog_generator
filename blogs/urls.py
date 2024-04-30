from django.urls import path
from .views import IndexView, get_blog, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("get-blog/", view=get_blog, name="get-blog"),
    path("blogs/", view=BlogListView.as_view(), name="blog-list"),
    path("blogs/<int:pk>/", view=BlogDetailView.as_view(), name="blog-detail"),
    path("blogs/<int:pk>/update/", view=BlogUpdateView.as_view(), name="blog-update"),
    path("blogs/<int:pk>/delete/", view=BlogDeleteView.as_view(), name="blog-delete"),
]
