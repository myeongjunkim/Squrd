from django.shortcuts import render, redirect
from .models import Post

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
        new_post.save()
        return redirect('feed')