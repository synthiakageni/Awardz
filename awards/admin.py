from django.contrib import admin

# Register your models here.
from .models import Profile, Project, Rate

admin.site.register(Profile)
admin.site.register( Project)
admin.site.register( Rate)
