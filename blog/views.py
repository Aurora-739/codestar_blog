from django.shortcuts import render
from blog import models
from django.views import generic
from models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"