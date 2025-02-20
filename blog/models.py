from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()

class Userinfo(models.Model):
    user = models.ForeignKey(User, null=True, blank=True ,on_delete = models.CASCADE)
    clientip=models.CharField(max_length=50)
    clientname=models.CharField(max_length=50)
    clientcount=models.IntegerField(default=100)
    clienttime=models.DateTimeField(auto_now_add=True)
    clienturl=models.CharField(max_length=200)
    clientview = models.CharField(max_length=200) 