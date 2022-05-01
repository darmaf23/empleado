from dataclasses import fields
from multiprocessing import context
from pipes import Template
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView

) 

from .models import Empleado

class ListAllEmpleado(ListView):
    template_name ='persona/list_all.html'
    paginate_by=4
    model =Empleado
    context_object_name = 'empleados'

    def get_queryset(self):
        print('***************')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista


class ListEmpleadosAdmin(ListView):
    template_name ='persona/list_empleados.html'
    paginate_by=10
    ordering ='first_name'
    model =Empleado
    context_object_name = 'empleados'

  


class ListByAreEmpleados(ListView):
    """lista de empleados de una Area"""
    template_name = "persona/list_by_area.html"
    context_object_name= 'empleados'
 
    def get_queryset(self):
        #el codigo que yo quiero
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista




class EmpleadoCreateView(CreateView):
    template_name = "persona/add-empleado.html"
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:lista-admin')


class succesview(TemplateView):
    template_name = "persona/success.html"


class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'

class ListEmpleadosByKword(ListView):
    template_name ='persona/by_kword.html'
    context_object_name ='hola'

    def get_queryset(self):
        print('***************')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self,**kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model =Empleado

    fields =[
        'first_name',
        'last_name',
        'job',
        'departamento',
        
    ]

    success_url = reverse_lazy('persona_app:lista-admin')

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model =Empleado
    success_url = reverse_lazy('persona_app:lista-admin')