from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from accounts.models import User


# Create your views here.
def view_feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {"posts":posts})

def create_post(request):
    if request.method == "POST":
        new_post = Post()
        new_post.main_img = request.FILES['post_image']
        new_post.textbody = request.POST['post_textbody']
        new_post.user = request.user
        user = get_object_or_404(User, id = request.user.id)
        user.point += 5
        user.save()
        new_post.save()
        return redirect('feed')