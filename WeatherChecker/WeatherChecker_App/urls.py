from django.contrib import admin
from django.urls import path,include
from WeatherChecker_App import views

urlpatterns = [
    path('', views.index, name='Index',kwargs = {'navbar': 'Index'}),
    path('home/', views.index, name='Index',kwargs = {'navbar': 'Index'}),
    path('login/', views.login, name='Login',kwargs = {'navbar': 'Login'}),
    path('signup/', views.signup, name='Signup',kwargs = {'navbar': 'Signup'}),
    path('signup-submit/', views.signupSubmit, name='signup-submit'),
    path('login-submit/', views.loginSubmit, name='login-submit')
]