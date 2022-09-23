from operator import index
from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    # if no value is passed in the url, it will lead to home page
    path('', views.index, name='Home'),
    # to get Two values in the url which will call the function
    path('<int:a>/<int:b>', views.bin)
]