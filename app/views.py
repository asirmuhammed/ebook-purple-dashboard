# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class Index(TemplateView):
    template_name = "index.html"
    
class Form(TemplateView):
    template_name = "pages/basic_elements.html"
    
class Icon(TemplateView):
    template_name = "pages/icon.html"
    
class Button(TemplateView):
    template_name = "pages/buttons.html"
    
class Typography(TemplateView):
    template_name = "pages/typography.html"
    
class Chart(TemplateView):
    template_name = "pages/chartjs.html"
    
class Table(TemplateView):
    template_name = "pages/tables.html"
    
class Error(TemplateView):
    template_name = "pages/error-404.html"
    
