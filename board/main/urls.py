from django.contrib import admin
from django.urls import path
from main.views import *



urlpatterns = [
    path('', main, name="main"),
    path('main2/', main2, name="main2"),
    path('main3/', main3, name="main3"),
    path('create/', create, name='create'),
    path('delete/<str:id>', delete, name='delete'),
    path('<str:id>', detail, name='detail'),
    
]