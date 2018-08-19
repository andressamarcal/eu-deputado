from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
import requests

class HomeView(TemplateView):
    template_name = "index.html"
