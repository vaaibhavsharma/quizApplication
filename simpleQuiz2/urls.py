from django.contrib import admin
from django.urls import path
from quiz.views import answerView, onboardingView, concludeView, profile, ChangePasswordView, firstQuestion
from userProfile.views import signUpView, winnerView,leaderboardView
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
urlpatterns = [
    path('notforyouok22/', admin.site.urls),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'),name="logout"),
    path('signup/',signUpView,name="signup"),
    path('winner/',winnerView,name='winner'),
    path('instructions/',TemplateView.as_view(template_name='instructions.html'),name='instructions'),
    path('quiz/',answerView,name="quiz"),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('leaderboard/',leaderboardView,name='leaderboard'),
    path('winner/',TemplateView.as_view(template_name='winner.html'),name='winner'),
    path('conclude/',concludeView,name='conclude'),
    path('profile/',profile,name='profile'),
    path('prestart/',TemplateView.as_view(template_name='prestart.html'),name='prestart'),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('onboarding/', onboardingView, name='onboarding'),
    path('quiz/level2/', firstQuestion, name='firstQuestion'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
