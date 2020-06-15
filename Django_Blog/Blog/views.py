from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
        'aurthor': 'CoreyMS',
        'Title': 'Blog Post 1',
        'Content': 'First Post Content',
        'Date_Posted': 'June 15,2020',

    },
    {
        'aurthor': 'Rivesh',
        'Title': 'Blog Post 2',
        'Content': 'Second Post Content',
        'Date_Posted': 'June 01,2020',

    },
    {
        'aurthor': 'Sherly',
        'Title': 'Blog Post 3',
        'Content': 'Third Post Content',
        'Date_Posted': 'Jan 15,2020',

    }
]
def home(request):
    context={
        'post':posts
    }
    return render(request,'Blog/Home.html',context)
def About(request):
    return render(request,'Blog/About.html',{'title':'About'})
