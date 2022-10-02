from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile
import re
def signUpView(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if  form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect(reverse_lazy('onboarding'))
        else:
            return render(request,'registration/signup.html',{'form':form})
    else:
        form=SignupForm()
        return render(request,'registration/signup.html',{'form':form})

@login_required
def winnerView(request):
    winner=request.user.profile.winner
    if winner:
        return render(request,'winner.html')
    else:
        return redirect('/')

def leaderboardView(request):
    x=re.compile(r'<(.*?),(\d+)>')
    leaders=Profile.objects.filter(user__is_staff=False)
    dates_scores=[]
    for profile in leaders:
        dates_scores.append({"username":profile.name,"data":x.findall(profile.data),'correct':profile.correct,'finalScore':profile.score})
    
    return render(request,'leaderboard.html',{"data":dates_scores})