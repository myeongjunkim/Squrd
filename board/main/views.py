from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Content, Comment
# Create your views here.

def main(request):
    contents = Content.objects.all()
    return render(request, 'main.html', {'contents':contents})

def main2(request):
    contents = Content.objects.all()
    return render(request, 'main2.html', {'contents':contents})

def main3(request):
    contents = Content.objects.all()
    return render(request, 'main3.html', {'contents':contents})

def create(request):
    new_content = Content()
    new_content.title = request.POST['title']
    new_content.writer = request.POST['writer']
    new_content.body = request.POST['body']
    new_content.pub_date = timezone.now()
    new_content.save()


    return redirect('main')

def delete(request, id):
    delete_content = Content.objects.get(id= id)
    delete_content.delete()
    return redirect('main')

def detail(request, id):
    content = get_object_or_404(Content, pk = id)
    comments = Comment.objects.filter(post = id)

    if request.method == "POST":
        comment = Comment()
        comment.post = content
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
    return render(request, 'detail.html', {'content':content, 'comments':comments})

