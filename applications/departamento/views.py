from multiprocessing import context
from re import template
from django.shortcuts import render

from .models import Departamento

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView

) 
# Create your views here.

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name= 'departamentos'

