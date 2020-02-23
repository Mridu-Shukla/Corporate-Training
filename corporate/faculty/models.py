from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    desc = models.TextField()
    school = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.name