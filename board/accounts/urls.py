from django.contrib import admin
from django.urls import path
from accounts.views import *



urlpatterns = [
    path('', index, name="index"),
    path('signin', signin, name="signin"),
    path('logout/', signout, name="signout"),
    path('signup/', signup, name="signup"),

    # kakao login
    path("login/kakao/", kakao_login, name="kakao-login"),
    path(
        "login/kakao/callback/",
        kakao_login_callback,
        name="kakao-callback",
    )

]