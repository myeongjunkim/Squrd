from django.shortcuts import redirect, render
from django.utils import timezone
from .models import *
from pathlib import Path
import os

def article(request):
    update_time = timezone.now
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles':articles, "update_time":update_time})




# 업데이트 호출
def update_article(request):
    print(os.getcwd())
    f = open('crawling/makearticle.py')
    exec(f.read())
    f.close()
    return redirect('article')