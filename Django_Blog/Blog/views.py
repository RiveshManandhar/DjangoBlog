from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'Blog/Home.html')
def About(request):
    return render(request,'Blog/About.html')
