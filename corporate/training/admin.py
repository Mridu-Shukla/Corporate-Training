from django.contrib import admin
from .models import Training, Topic, Comment

# Register your models here.

admin.site.register(Topic)
admin.site.register(Training)
admin.site.register(Comment)
