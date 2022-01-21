from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Vote_post)
admin.site.register(Participant)
admin.site.register(Comment)

