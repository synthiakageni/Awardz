import json
from decimal import Context
from django.contrib import messages
from django.contrib.auth import authenticate, forms, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.urls.base import reverse
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from .forms import (ProfileUpdateForm, ProjectForm, RateForm,
                    UserUpdateForm)
from .models import Profile, Project, Rate
from .token_generator import account_activation_token


class edit_profile(generic.UpdateView):
    model=Profile
    template='accounts/edit_profile.html'
    fields=['bio','profile_pic','twitter_url']
    success_url=reverse_lazy('')



  
def logout(request):
    if request.method == "POST":
        logout(request) 
def view_profile(request):
 
    return render (request, "accounts/profile.html")  
              
def editProfile(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form=UserUpdateForm(instance=request.user)   
        profile_form=ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form":user_form,
        "profile_form":profile_form,
        
    }
    return render (request, "accounts/edit_profile.html",context)  
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('welcome')  


def new_project(request):
   
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
           
            project.save()
            return redirect('welcome')

    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})   
def view_projects(request):
    project=Project.all_projects()
    form=ProjectForm()
    return render(request, 'index.html',{"project":project,"form":form})




def rate_project(request,id):
    # reviews = Revieww.objects.get(projects_id = id).all()
    # print
    
    project = Project.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)     

        if form.is_valid():
            data = form.cleaned_data
           
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
          
            return redirect('welcome')
    else:
        form = RateForm()
    return render(request,"ratings/rate.html",{"form":form,"project":project})        




def search_results(request):
       if 'project' in request.GET and request.GET["project"]:
              search_term=request.GET.get("project")
              searched_projects =Project.search_project(search_term)
              message=f"{search_term}"
              
              return render(request, 'search.html',{"message":message,"project": searched_projects })
       else:
              message="You haven't searched for any term"
              return render(request,'search.html',{"message":message})   

    
    
    

                