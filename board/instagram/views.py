import re
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from accounts.models import User
from django.contrib import messages


# Create your views here.
def view_feed(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    posts = Post.objects.all()
    return render(request, 'feed.html', {"posts":posts})

def view_mypage(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'mypage.html')
    

def update_mypage(request):
    if request.method == "POST":
        user = get_object_or_404(User, id = request.user.id)
        if request.FILES:
            user.profile_img = request.FILES['profile_img']
        user.name = request.POST['user_name']
        user.email = request.POST['user_email']
        user.save()
        return redirect('mypage')

def create_post(request):
    if request.method == "POST":
        new_post = Post()
        if request.FILES:
            new_post.main_img = request.FILES['post_image']
        new_post.textbody = request.POST['post_textbody']
        new_post.user = request.user
        user = get_object_or_404(User, id = request.user.id)
        user.point += 5
        user.save()
        new_post.save()
        return redirect('feed')

def insta_comment(request, id):
    if not request.user.is_authenticated:
        return redirect('signin')
    post = get_object_or_404(Post, pk = id)
    # 댓글 요청
    if request.method == "POST":
        comment = Insta_Comment()
        comment.user = request.user
        comment.posting = post
        comment.content = request.POST['body']
        comment.pub_date = timezone.now()

        # 답글 구분
        perent_comment_id = request.POST['perent_comment_id']
        if perent_comment_id:
            perent_comment = get_object_or_404(Insta_Comment, pk = perent_comment_id)
            comment.parent_comment = perent_comment
        comment.save()

        user = get_object_or_404(User, id = request.user.id)
        user.point += 5
        user.save()


    # 댓글 필터
    comments = Insta_Comment.objects.filter(posting = id)
    comments_list = []
    for comment in comments:
        if comment.parent_comment == None:
            recomments = Insta_Comment.objects.filter(parent_comment = comment.id)
            comments_list.append({"comment":comment, "recomments":recomments})

    return render(request, 'post_detail.html', {'vote_post':post, 'comments_list':comments_list})


# 메일
def view_mail(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'mail.html')

def send_mail(request):
    if request.method == "POST":
        mail_receiver = request.POST['mail_receiver']
        if User.objects.filter(username=mail_receiver).exists():
            new_mail = Mail()
            new_mail.receiver = get_object_or_404(User, username = mail_receiver)
            new_mail.sender = request.user
            new_mail.title = request.POST['mail_title']
            new_mail.textbody = request.POST['mail_textbody']
            new_mail.pub_date = timezone.now()
            messages.success(request, "메일을 성공적으로 보냈어요!")
        else:
            messages.error(request, "메일 전송에 실패했어요 받는 사람 아이디를 확인해 주세요")

        
        return redirect('mail')
        