from re import template
from django.shortcuts import render

from .models import Prueba

from . forms import PruebaForm

# Create your views here.
from django.views.generic import TemplateView,CreateView

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url ='.'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'
