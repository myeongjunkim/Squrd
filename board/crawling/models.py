from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    entertain_name = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title