from django.shortcuts import redirect, render
from django.utils import timezone
from .models import *
# from .makearticle import *

def article(request):
    # crawling_main()
    update_time = timezone.now
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles':articles, "update_time":update_time})

def update_article(request):
    # crawling_main()
    print(timezone.now)
    return redirect('article')
