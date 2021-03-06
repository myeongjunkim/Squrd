from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
# 얘가 디비에서 조회해서 있으면 가져오는 기특한 애
from django.contrib.auth import authenticate, login, logout
from .models import User
import json, os, requests


# secret key
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')


with open(SECRET_FILE) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    return secrets[setting]
    


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == "POST":
        input_id = request.POST['input_id']
        input_pw = request.POST['input_pw']
        user = authenticate(username=input_id, password=input_pw)
        if user is not None:
            login(request, user)

            user.point += 5
            user.save()
            messages.success(request, f"로그인 성공! 포인트 5점 획특! 현재 포인트 {user.point} 점" )

            return redirect('index')
        else:
            messages.error(request, "아이디와 비밀번호가 일치하지 않습니다. 다시 확인해 주세요")

            print("로그인 실패")
    return render(request, "signin.html")
    
def signup(request):
    if request.method == "POST":
        print("폼 동작")
        input_name = request.POST['input_name']
        input_id = request.POST['input_id']
        input_pw = request.POST['input_pw']
        input_pw_check = request.POST['input_pw_check']
        if User.objects.filter(username=input_id).exists():
            messages.error(request, "이미 존재하는 아이디 입니다. 다른 아이디를 입력해 주세요!" )
            return redirect("signup")

        else:
            if input_name != "" and input_id != "" and input_pw !="":
                if input_pw == input_pw_check:    
                    user = User.objects.create_user(input_id, input_id, input_pw)
                    user.name = input_name
                    user.save()
                    print("회원정보 디비 저장")
                    messages.success(request, "회원가입 성공! 로그인하여 입장해 주세요!" )
                    
                    return redirect("signin")
                else:
                    messages.error(request, "비밀번호와 비밀번호 확인이 일치하지 않습니다.")
                    return redirect("signup")
            else:
                messages.error(request, "아이디와 비밀번호를 입력해 주세요!")
                return redirect("signup")
    return render(request, "signup.html")


def signout(request):
    logout(request)
    messages.success(request, "로그아웃 되었습니다!" )
    return redirect('signin')

# kakao login

def kakao_login(request):
    client_id = get_secret('KAKAO_REST_KEY')
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    # REDIRECT_URI = "http://ec2-54-180-95-65.ap-northeast-2.compute.amazonaws.com:8080/accounts/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
    )

def kakao_login_callback(request):
    code = request.GET.get("code")
    client_id = get_secret('KAKAO_REST_KEY')
    client_secret = get_secret('CLIENT_SECRET')
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    # REDIRECT_URI = "http://ec2-54-180-95-65.ap-northeast-2.compute.amazonaws.com:8080/accounts/login/kakao/callback"
    #(2)
    token_request = requests.post(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}&client_secret={client_secret}",
            headers={"Accept": "application/json"},
        )
    #(3)
    token_json = token_request.json()
    access_token = token_json.get("access_token")
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()
    email = profile_json.get("kakao_account", None).get("email")
    if email is None:
        email = str(profile_json.get("id")) + "@kakao.com"
    print(profile_json, email)
    properties = profile_json.get("properties")
    nickname = properties.get("nickname")
    if User.objects.filter(username=email).exists():
        user = get_object_or_404(User,username=email)
    else:
        user = User.objects.create(
            email=email,
            username=email,
            name=nickname
        )
        user.set_unusable_password()
        user.save()
    login(request, user)
    user.point += 5
    user.save()
    messages.success(request, f"로그인 성공! 포인트 5점 획특! 현재 포인트 {user.point} 점" )
    return redirect(reverse("index"))

    
    