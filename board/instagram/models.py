from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    main_img = models.ImageField(null=True, upload_to="instagram/", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    textbody = models.TextField()    

