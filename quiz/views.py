from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import AnswerForm, UpdateUserForm, UpdateUserForm_two
from .models import Question, inputQuestions
from django.contrib.auth.views import PasswordChangeView
import json
import random

from google.oauth2 import id_token
from google.auth.transport import requests

from datetime import datetime,timedelta
import time
import pytz
# Create your views here.

#--------------Globals-------------------#
IST = pytz.timezone('Asia/Kolkata') 
starttime = IST.localize(datetime(2022,3,12,21,00,0,0))
endtime = IST.localize(datetime(2023,3,13,22,0,0,0))
#----------------------------------------#

# Custom Error Messages

randomMessages = [
    'Sorry, You Need To Think Harder.',
    'Close enough, or are you?',
    'Tired of guessing the wrong answer? Try writing the correct one',
    'Might be the right time to put on that thinking cap',
    'Psst, sure you Googled it correct?',
    'tch tch',
    'Did you try Elon Musk though?',
    'You know, they say Blockchain is the answer to everything',
    'We can neither confirm nor deny that you\'re on the right track',
    'get clever guys, show why it\'s an ACM event'
]
#bad Word List (Custom Messages for bad Words

galikilist  = [
    'fuck'
]

requestMessages = [
    'pleasehelpme',
    'godhelpme',
    'iamwinner',
    'correctanswer',
    'acmforthewin'
    'acmftw',
    'pleasehelpmebaby',
    'baby',
    'pleasehelp'
    'help',
    'daddy',
]

@login_required
def answerView(request):
    profile=request.user.profile
    
    
    if profile.verifed == False:
        return redirect(reverse_lazy('onboarding'))
    if datetime.now(tz=IST) < starttime:
        return redirect(reverse_lazy('prestart'))
    elif datetime.now(tz=IST) > endtime:
        return redirect(reverse_lazy('conclude'))
    else:
        old_id = profile.ques_id
        print()
     
        if request.is_ajax() and request.method=="POST":
            form=AnswerForm(request.POST)
            if form.is_valid():
                tempAnswer=form.cleaned_data.get('answer')
                if tempAnswer != None:
                    try:
                        inputQuestions.objects.create(
                            user=profile.user,
                            question=profile.ques_id,
                            textAnswer=tempAnswer,
                            ipaddress=request.META.get("REMOTE_ADDR"),
                        )
                    finally:
                        pass
                    if tempAnswer.lower() in requestMessages:
                        eM =  [
                            "Contact @Vaibhav with screenshot",
                            "Contact @Bhavya with screenshot",
                            "Contact @Aarhan with screenshot",
                            "Contact @Devansh with screenshot",
                        ]
                        if tempAnswer.lower() == "hater":
                            errorM = eM[0]
                        else:
                            errorM = random.choice(eM)

                        data={'correct':False, 'errorM': errorM}
                        return JsonResponse(data)
                    elif tempAnswer.lower() == "motivation" or tempAnswer.lower() == "iloveyou":
                        errorM = "But Little Motivation! <3"
                        data = {'correct': False, 'errorM': errorM, 'customCode': 10}
                        return JsonResponse(data)
                    elif tempAnswer.lower() in galikilist:
                        errorM = "https://youtu.be/dQw4w9WgXcQ?t=1"
                        data = {'correct': False, 'errorM': errorM, 'customCode': 20}
                        return JsonResponse(data)
                        
                    if tempAnswer.lower().startswith("flag{") != True:
                        data = {'correct': False, 'errorM': "Submit in format Flag{Your_Answer}"}
                        return JsonResponse(data)
                    else:
                        actualAnswer=getObj(profile).answer
                        
                        if  tempAnswer.lower() == actualAnswer.lower():
                            profile.ques_id+=1
                            profile.correct+=1
                            profile.score+=10
                            profile.data+='<'+str(datetime.now(tz=IST).isoformat())+','+str(profile.score)+'>'
                            profile.lastQuestionTime = datetime.now(tz=IST)
                            profile.save()
                        
                        winner=checkForWin(profile)
                        if winner:
                            data={'winner':winner}
                        else:
                            profileObj=getObj(profile)
                            question={'text':profileObj.question}
                            if(profile.lastQuestionTime != None):
                                print(datetime.now(tz=IST) - profile.lastQuestionTime)
                            if(profile.ques_id == old_id):
                                randomMess = random.choice(randomMessages)
                                data={'question':question,'winner':winner,'correct':False, 'errorM': randomMess}
                            else:
                                data={'question':question,'winner':winner,'correct':True}
                        return JsonResponse(data)
                else:
                    data = {'None': 'Yes'}
                    return JsonResponse(data)
            else:
                data = {'None': 'Yes'}
                return JsonResponse(data)
        else:
            if checkForWin(profile):
                return redirect(reverse_lazy('winner'))
            form=AnswerForm()
            profileObj=getObj(profile)
            question={'text':profileObj.question, 'asset': profileObj.asset, 'questionNum': profileObj.questionNumber}
            hint = profileObj.hint
            if hint:
                return render(request, 'quiz.html', {'question': question, 'form': form, 'hint': hint})
            else:
                return render(request,'quiz.html',{'question':question,'form':form})

@login_required
def getObj(profile):
    # while True:
    #     try:
    #         quesObj=Question.objects.get(questionNumber=profile.ques_id)
    #     except ObjectDoesNotExist:
    #         profile.ques_id+=1
    #         profile.save()
    #         continue
    #     else:
    #         break
    quesObj = Question.objects.get(questionNumber=profile.ques_id)
    return quesObj
    
@login_required
def checkForWin(profile):
    if profile.correct == profile.total_ques:
        profile.winner=True
        profile.save()
        return True
    else:
        return False

@login_required
def onboardingView(request):
    profile = request.user.profile
    if profile.verifed:
        return redirect(reverse_lazy('quiz'))

    if request.is_ajax() and request.method == "POST":
        token = request.POST["credential"]
        CLIENT_ID = request.POST["clientId"]
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        if idinfo['email'] == profile.user.email and idinfo['hd'] == '@gmail.com': # Your Custom Domain
                profile.verifed = True
                profile.name = idinfo['name']
                profile.save()
                data = {'status': True, 'message': "Succesfully Verified!!"}
        else:
            data = {'status': False, 'message': "Try Again Or Use Correct EmailID!"}
        return JsonResponse(data)
    return render(request, 'onboarding.html')

@login_required
def concludeView(request):
    if datetime.now(tz=IST) < endtime:
        return redirect(reverse_lazy('home'))

    return render(request, 'conclude.html')

@login_required
def firstQuestion(request):
    profile = request.user.profile
    print(profile.ques_id)
    if profile.ques_id == 1:
        profile.ques_id += 1
        profile.correct += 1
        profile.score += 10
        profile.data += '<' + str(datetime.now(tz=IST).isoformat()) + ',' + str(profile.score) + '>'
        profile.lastQuestionTime = datetime.now(tz=IST)
        profile.save()
    return redirect(reverse_lazy('quiz'))




@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.profile.verifed == True:
            user_form = UpdateUserForm_two(request.POST, instance=request.user)
        else:
            user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse_lazy('profile'))
    else:
        user_form = UpdateUserForm(instance=request.user)
    if request.user.profile.verifed == False:
        return render(request, 'profile.html', {'user_form': user_form, 'verifed': False})
    else:
        return render(request, 'profile.html', {'user_form': user_form, 'verifed': True})


@login_required
def timeOut_check(request):
    profile = request.user.profile
    if request.method=='POST':
        print(request.POST['interval'])
        x =request.POST['interval']
        if int(x) == 0:
            profile.ques_id+=1
            print(profile.ques_id)
            print(request.POST['interval'])
            
            #profile.ques_id += 1
            
            
            profile.save()
            profileObj=getObj(profile)
            question={'text':profileObj.question}
            print(question)
        return redirect(reverse_lazy('quiz'))
        
class ChangePasswordView(PasswordChangeView):
    template_name = 'passwordchange.html'
    success_url = reverse_lazy('profile')


