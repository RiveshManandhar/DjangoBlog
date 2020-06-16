from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context={
        'post':Post.objects.all()
    }
    return render(request,'Blog/Home.html',context)
def About(request):
    return render(request,'Blog/About.html',{'title':'About'})
