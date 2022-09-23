from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.mission, name='home'),
]