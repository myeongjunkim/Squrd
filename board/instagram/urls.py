from django.contrib import admin
from django.urls import path
from instagram.views import *



urlpatterns = [
    path('', view_feed, name="feed"),
    path('insta-comment/<str:id>', insta_comment, name="insta_comment"),
    path('create-post', create_post, name="create_post"),
    path('mypage', view_mypage, name="mypage"),
    path('update-mypage', update_mypage, name="update_mypage"),
    path('mail', view_mail, name="mail"),
    path('send-mail', send_mail, name="send_mail"),
    path('detail-mail/<str:id>', detail_mail, name="detail_mail"),




    
]