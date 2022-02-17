from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=20)
    
class Mypage(models.Model):
    profile_img = models.ImageField(null=True, upload_to="accounts/", blank=True)
    point = models.IntegerField(null= True, default=0)
    color = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
