from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'


