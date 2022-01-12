from django.contrib import admin
from django.urls import path
from crawling.views import *



urlpatterns = [
    path('', article, name="article"),
    path('update_article/', update_article, name="update_article"),
    
    
    
]