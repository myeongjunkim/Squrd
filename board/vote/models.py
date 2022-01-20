# from django.db import models

# # Create your models here.
# class Vote_post(models.Model):
#     title = models.TextField(max_length=40, null=True)
#     imgfile_1 = models.ImageField(null=True, upload_to="", blank=True)
#     img_name_1 = models.TextField(max_length=20)
#     imgfile_2 = models.ImageField(null=True, upload_to="", blank=True)
#     img_name_2 = models.TextField(max_length=20)
#     pub_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Participant(models.Model):
#     ip = models.TextField(max_length=40)
#     choice = 1
#     vote_post = models.ForeignKey(Vote_post, on_delete=models.CASCADE, null=True)
#     pub_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.ip


# class Comment(models.Model):
#     content        = models.CharField(max_length=500)
#     pub_date       = models.DateTimeField(auto_now_add=True)
#     user           = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
#     posting        = models.ForeignKey('Vote_post', on_delete=models.CASCADE)
#     parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table = 'comments'