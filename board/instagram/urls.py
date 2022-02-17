from django.contrib import admin
from django.urls import path
from instagram.views import *



urlpatterns = [
    path('', view_feed, name="feed"),
    
]