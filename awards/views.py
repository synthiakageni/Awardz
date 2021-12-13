from django.shortcuts import render
from decimal import Context
from django.contrib.auth import forms
from django.shortcuts import render,redirect,get_object_or_404
from  django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.urls import reverse
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from .forms import UserSignUpForm,UserUpdateForm,ProfileUpdateForm,ProjectForm,RatingForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView
from .models import Profile,Project,Rate
from django.contrib.auth.mixins import LoginRequiredMixin
class edit_profile(generic.UpdateView):
    model=Profile
    template='accounts/edit_profile.html'
    fields=['bio','profile_pic','twitter_url']
    success_url=reverse_lazy('')

    def signup(request):
     if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link=reverse('activate',kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)})
            activate_url='http://'+domain+link
            
            email_body='Hi ' +user.username+ ' Please use this link to verify your account\n' +activate_url
            
            email_subject = 'Activate Your Account'
            
            to_email = form.cleaned_data.get('email')
            
            email = EmailMessage(email_subject, email_body, 'francis.kinyae@student.moringaschool.com',[to_email])
            
            email.send()
            
            return HttpResponse('We have sent you an email, please confirm & activate your email address to complete registration')
     else:
        
        form = UserSignUpForm()
     return render(request, 'accounts/signup.html', {'form': form})
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activate successfully')
        
    else:
        return HttpResponse('Activation link is invalid!')
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        
        user = authenticate(request, password=password, username=username)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "stages/accounts/login.html",context)
        login(request,user)
def logout(request):
    if request.method == "POST":
        logout(request)        