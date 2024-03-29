from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . forms import CustomUsertCreationForm
# Create your views here.
class SignUpViews(generic.CreateView):
    form_class = CustomUsertCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')