from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Capitals


class HomePageView(ListView):
    template_name = "home.html"
    model = Capitals


class NewCapitalView(CreateView):
    template_name = "capital_new.html"
    model = Capitals
    fields = ["city", "country"]


# Create your views here.
