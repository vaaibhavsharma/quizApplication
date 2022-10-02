  
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from quiz.models import Question
from .models import Profile
from django.db.models import F

@receiver(post_save,sender=User)
def createUserProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=Question)
def incrementTotal(sender,created,**kwargs):
    if created:
        for profile in Profile.objects.all():
            profile.total_ques+=1
            profile.save()

@receiver(post_delete,sender=Question)
def decrementTotal(sender,**kwargs):
    Profile.objects.all().update(total_ques=F('total_ques') - 1)