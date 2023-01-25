from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = 'article'
    template_name = 'posts.html'
    context_object_name = 'posts'