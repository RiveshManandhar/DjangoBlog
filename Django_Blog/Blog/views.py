from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'Blog/Home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/Home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


def About(request):
    return render(request, 'Blog/About.html', {'title': 'About'})

