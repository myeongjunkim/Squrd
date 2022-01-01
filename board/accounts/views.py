from django.shortcuts import render, redirect
# 얘가 디비에서 조회해서 있으면 가져오는 기특한 애
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signin(request):
    if request.method == "POST":
        input_id = request.POST['input_id']
        input_pw = request.POST['input_pw']
        user = authenticate(username=input_id, password=input_pw)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            print("로그인 실패")
    return render(request, "signin.html")
    
def signup(request):
    return render(request, "signup.html")

def signout(request):
    logout(request)
    return redirect('signin')
