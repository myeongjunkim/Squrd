from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', view_vote, name="view_vote"),
    path('create-vote/', create_vote, name="create_vote"),
    path('delete-vote/<str:id>', delete_vote, name="delete_vote"),
    # path('create-comment/<str:id>', create_comment, name="create_comment"),
    path('view-comment/<str:id>', view_comment, name="view_comment"),
    path('create-participant/', create_participant, name="create_participant"),
    
]