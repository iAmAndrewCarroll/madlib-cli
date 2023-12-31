from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Snack

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class HomePageView(TemplateView):
    template_name = 'home.html'

# Create your views here.
