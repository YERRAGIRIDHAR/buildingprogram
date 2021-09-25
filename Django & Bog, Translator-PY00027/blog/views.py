from django.shortcuts import render
from .models import Post #Name of the class in models.py
from django.views import generic #To get  as view attribute in line 5 url.py in blog folder
# Create your views here.
class BlogView(generic.DetailView): #detailview is having as_view in it
    model =  Post #Name of the class in model.py
    template_name = 'blog.html' #Name of the html file

class AboutView(generic.TemplateView): #creating a class for about page
    template_name = 'about.html'
    
class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-date_created')#creating a class for postlist page order by date which are published
    template_name = 'index.html'  
