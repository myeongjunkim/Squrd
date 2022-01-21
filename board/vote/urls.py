from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', view_vote, name="vote"),
    path('create_vote/', create_vote, name="create_vote"),
    
]