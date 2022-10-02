from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question=models.TextField()
    answer=models.CharField(max_length=200)
    hint = models.CharField(max_length=200, null=True, blank=True)
    asset=models.URLField(max_length=500,verbose_name='assets', null=True, blank=True)
    questionNumber = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.question[:50]}...'

class inputQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    textAnswer = models.CharField(max_length=200)
    textTime = models.TimeField(auto_now=True)
    ipaddress = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return f'{self.user} on {self.textTime} answered = {self.textAnswer}'

