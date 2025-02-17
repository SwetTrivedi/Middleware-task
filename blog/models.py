from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()

class Userinfo(models.Model):
    clientip=models.IntegerField()
    clientname=models.CharField(max_length=50)
    clientcount=models.IntegerField()
    clienttime=models.DateTimeField()