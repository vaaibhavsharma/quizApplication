from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
class SignupForm(UserCreationForm):
    email=forms.EmailField()
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    ,required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2','captcha']