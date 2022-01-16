from django.shortcuts import redirect, render
from django.utils import timezone
from .models import *
from pathlib import Path
import os
from .makearticle import crawling_main, ENTERTAIN



def article(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles':articles})




# 업데이트 호출
def update_article(request):
    crawling_main()
    return redirect('article')

print("왜 호출됨?")
