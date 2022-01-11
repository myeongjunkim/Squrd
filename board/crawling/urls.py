from django.contrib import admin
from django.urls import path
from crawling.views import *



urlpatterns = [
    path('', article, name="article"),
    
    
]