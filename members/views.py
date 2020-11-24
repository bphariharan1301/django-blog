
from .forms import SignUpForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')



