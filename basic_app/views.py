from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView 

class Registration(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('users:login')
    template_name='basic_app/registration.html'