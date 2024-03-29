from django.db import models
from app.models import *

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    url=models.URLField()


class AccessRecords(models.Model):
    ename=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()