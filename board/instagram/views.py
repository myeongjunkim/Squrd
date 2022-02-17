from django.shortcuts import render

# Create your views here.
def view_feed(request):
    return render(request, 'feed.html')