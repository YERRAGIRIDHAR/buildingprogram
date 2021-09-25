from django.views.generic.base import View
from . import views # . means from current directory import views
from django.urls import path

urlpatterns = [
    path('', views.translator_view, name = 'translator_view') #calling postlist method from views
]