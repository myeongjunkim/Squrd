from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    main_img = models.ImageField(null=True, upload_to="instagram/", blank=True, default='instagram/board1.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    textbody = models.TextField()    

class Insta_Comment(models.Model):
    content        = models.CharField(max_length=500)
    user           = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    posting        = models.ForeignKey('Post', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    pub_date       = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'insta_comment'

class Mail(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sender = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    textbody = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
