from django.shortcuts import render

# Create your views here.
def view_vote(request):
    return render(request, 'vote.html')