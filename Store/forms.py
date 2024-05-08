from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Regi(UserCreationForm):
    class Meta:
        model=User
        
        fields=['username','first_name','last_name','email','password1','password2']
        
        # username= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
        # first_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
        # last_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
        # email= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
        # password1= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
        # password2= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))

           


class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class orderform(forms.Form):
     address= forms.CharField(widget=forms.Textarea)
    