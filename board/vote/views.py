from django.shortcuts import render, redirect
from .models import Vote_post, Comment, Participant

# Create your views here.
def view_vote(request):
    vote_posts = Vote_post.objects.all()
    # vote_posts_list=[]
    # for vote_post in vote_posts:
    #     comments = Comment.objects.filter(posting = vote_post.id)
    #     comments_list = []
    #     for comment in comments:
    #         if comment.parent_comment is None:
    #             recomments = Comment.objects.filter(parent_comment = comment.id)
    #             comments_list.append({"comment":{"recomments":recomments}})
    #     vote_posts_list.append({"vote_post":vote_post, "comments_list":comments_list})

    # return render(request, 'vote.html', {"vote_posts_list":vote_posts_list} )
    return render(request, 'vote.html', {"vote_posts":vote_posts})


def create_vote(request):
    vote_post = Vote_post()
    data = request.POST
    vote_post.title = data['title']
    vote_post.imgfile_1 = request.FILES['img1']
    vote_post.img_name_1 = data['name1']
    vote_post.imgfile_2 = request.FILES['img2']
    vote_post.img_name_2 = data['name2']
    vote_post.save()
    return redirect('vote')
