from django.db import models
from django.utils import timezone

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summeray(self):
        return self.body[:50]

class Comment(models.Model):
    post = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)
    # writer = models.CharField(max_length=20, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body






class Content2(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summeray(self):
        return self.body[:50]

class Comment2(models.Model):
    post = models.ForeignKey(Content2, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class Content3(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summeray(self):
        return self.body[:50]

class Comment3(models.Model):
    post = models.ForeignKey(Content3, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)