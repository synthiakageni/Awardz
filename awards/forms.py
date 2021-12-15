from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import UpdateView
from .models import Profile,Project, Rate


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = [
            'bio',
            'profile_pic',
            'twitter_url'
        ] 
class ProfileUpdateForm(forms.ModelForm):
            class Meta:
                model=Profile
                fields = ['bio','profile_pic','twitter_url']    

                    
class UserUpdateForm(forms.ModelForm):
            class Meta:
                model=User
                fields = ['username','email']                
       
       
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project  
        fields = ['title','url','description','photo']     
        
class RateForm(forms.ModelForm):
    class Meta:
        model=Rate 
        fields = ['design','usability','content']       
 

