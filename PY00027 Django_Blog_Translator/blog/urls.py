from django.views.generic.base import View
from . import views # . means from current directory import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name = 'blog_view'),
    path('about/', views.AboutView.as_view(), name = 'about_view'),
    path('', views.PostList.as_view(), name = 'home') #calling postlist method from views
]