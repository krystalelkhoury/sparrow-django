from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'pages/login/signup.html'

class Login(LoginView):
    success_url = reverse_lazy('login')
    template_name = 'pages/login/login.html'


class AdminDashboard(generic.View):
    #success_url = reverse_lazy('dashboard')
    template_name = 'pages/dashboard/dashboard.html'


class EmployeeDashboard(generic.View):
    #success_url = reverse_lazy('login')
    template_name = 'pages/common/sidebar_template.html'
