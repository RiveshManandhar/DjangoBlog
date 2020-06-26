from django.urls import path
from . import views
from .views import PostListView, PostDetailView
urlpatterns = [
    #path('', views.home, name='blog_home'),
    path('', PostListView.as_view(), name='blog_home'),
    path('About/', views.About, name='blog_About'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]