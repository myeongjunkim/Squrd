from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=20)
    profile_img = models.ImageField(null=True, upload_to="accounts/", blank=True, default='accounts/person.png')
    point = models.IntegerField(null= True, default=0)
    color = models.CharField(null= True, default="black", max_length=20)
