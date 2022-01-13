from django.shortcuts import redirect, render
from django.utils import timezone
from .models import *
from pathlib import Path
import os

def article(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles':articles})




# 업데이트 호출
def update_article(request):
    
    return redirect('article')