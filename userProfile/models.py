  
from django.db import models
from django.contrib.auth.models import User
from quiz.models import Question
# Create your models here.

class Profile (models.Model):
    def num_ques():
        return Question.objects.all().count()
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True, blank=True)
    ques_id=models.IntegerField(verbose_name='Question At',default=1)
    score=models.IntegerField(default=0)
    data=models.TextField(default="March 12, 2022 21:00:00")
    correct=models.IntegerField(default=0)
    total_ques=models.IntegerField(verbose_name='Total Questions',default=num_ques)
    winner=models.BooleanField(default=False)
    verifed = models.BooleanField(default=False)
    lastQuestionTime = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering=['-score']
        
    def __str__(self):
        return self.user.username