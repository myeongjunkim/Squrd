from django.shortcuts import render, redirect, get_object_or_404
from .models import Vote_post, Comment, Participant
from django.utils import timezone
from requests import get
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
def view_vote(request):
    vote_posts = Vote_post.objects.all()

    userIP = get('https://api.ipify.org').text
    print(userIP)
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
    return redirect('view_vote')

def delete_vote(request,id):
     delete_vote_post = Vote_post.objects.get(id= id)
     delete_vote_post.delete()
     return redirect('vote')


def view_comment(request, id):
    vote_post = get_object_or_404(Vote_post, pk = id)
    # 댓글 요청
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.posting = vote_post
        comment.content = request.POST['body']
        comment.pub_date = timezone.now()

        # 답글 구분
        perent_comment_id = request.POST['perent_comment_id']
        if perent_comment_id:
            perent_comment = get_object_or_404(Comment, pk = perent_comment_id)
            comment.parent_comment = perent_comment
        comment.save()

    # 댓글 필터
    comments = Comment.objects.filter(posting = id)
    comments_list = []
    for comment in comments:
        if comment.parent_comment == None:
            recomments = Comment.objects.filter(parent_comment = comment.id)
            comments_list.append({"comment":comment, "recomments":recomments})

    return render(request, 'comment.html', {'vote_post':vote_post, 'comments_list':comments_list})


# ajax api about main vote

def create_participant(request):
    user_ip = get('https://api.ipify.org').text
    data = request.GET
    choice = data['result']
    vote_post_id = data['votePostId']

    # 중복 잡기
    queryset = Participant.objects.filter(ip = user_ip)
    vote_post = get_object_or_404(Vote_post, pk = vote_post_id)
    # vote_post.id 가 겹치는지
    for v in queryset:
        if v.vote_post == vote_post:
            return HttpResponse('overlap')
        # print("투표자가 투표한거",v.vote_post, vote_post)

    print(user_ip)
    print(choice)
    
    
    participant = Participant()
    participant.ip = user_ip
    participant.choice = choice
    participant.vote_post = vote_post
    participant.save()


    return HttpResponse('create')


def vote_total(request):
    vote_post_id = int(request.GET["votePostId"])
    participants = Participant.objects.filter(vote_post = vote_post_id)
    first_cnt = 0
    second_cnt = 0
    for p in participants:
        if p.choice == "First":
            first_cnt +=1
        elif p.choice == "Second":
            second_cnt +=1
    data = {
        "total":len(participants),
        "first":{"cnt":first_cnt,"per":round(100*first_cnt/len(participants),1)},
        "second":{"cnt":second_cnt,"per":round(100*second_cnt/len(participants),1)},
    }

    return JsonResponse(data)
    
