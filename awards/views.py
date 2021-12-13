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

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView
from .models import Profile,Project,Rate
from django.contrib.auth.mixins import LoginRequiredMixin
