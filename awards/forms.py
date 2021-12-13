from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import UpdateView
from .models import Profile,Project, Rate

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text='Required')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

