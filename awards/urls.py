from django.urls import path,include 
from . import views
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/login/', views.login, name='login'),
    path('', views.view_projects, name='welcome'),
    path('accounts/signup/', views.usersignup, name='signup'),
    path('activate/<uidb64>/<token>/',
        views.activate_account, name='activate'),
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.PasswordsChangeView.as_view(), name='password_change'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
     
    path('edit_profile/',views.editProfile,name='edit_profile'),
    path('projects/',views.new_project,name='projects'),
    path('rate/<int:id>/',views.rate_project,name='rate_projects'),
    path('search/', views.search_results, name='search_results'),
    path('accounts/profile/',views.view_profile, name='profile'), 

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)