from django.contrib import admin
from django.urls import path
from accounts.views import *



urlpatterns = [
    path('', signin, name="signin"),
    path('logout/', signout, name="signout"),
    path('signup/', signup, name="signup"),
]