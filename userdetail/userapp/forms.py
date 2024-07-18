from django import forms
from django_recaptcha.fields import ReCaptchaField
from userapp.models import userdata,rd_amount
from django.contrib.auth.models import User


class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class userprofile(forms.ModelForm):
    class Meta:
        model=userdata
        fields=['img','user_url']

    captcha = ReCaptchaField()
class UserUpdatedform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

class rate_of_int(forms.ModelForm):
    class Meta:
        model=rd_amount
        fields=['total_amount','amount','noof_year','interst_amt','rate_of_interest','total_investement','total_returns']

