from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import UpdateView
from .models import Profile,Project, Rate
