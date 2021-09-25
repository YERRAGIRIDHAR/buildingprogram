from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, 'Draft'),(1, 'Publish'))

class Post(models.Model): #Class(post) inherits from models.Model class
    title = models.CharField(max_length=200) #Title is the field of database Post having charcter type with max len of 200 chars
    content = models.TextField()#content is the field of database Post having text type
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, ) #Forienkey used for author because it comes from another database
    #when user deleted from database user content also deleted thats what cascade do
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self) -> str:
        return self.title #to give the name as title in the post column