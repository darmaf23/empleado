from django.contrib import admin
from django.urls import path

from . import views

app_name="persona_app"

urlpatterns = [
     path(
        '',
         views.InicioView.as_view(),
         name='inicio'),
    path('prueba-todo-empleados',
          views.ListAllEmpleado.as_view(),
          name='listar-todo'),

    path('buscar-empleado/',
            views.ListEmpleadosByKword.as_view(),
            name='lista-kword'
     ),


    path('lista-area/<shorname>/',
        views.ListByAreEmpleados.as_view(),
        name='empleados_area'),

    path('lista-empleados-admin/',
        views.ListEmpleadosAdmin.as_view(),
        name='lista-admin'),

    path('ver-empleados/<pk>/', 
            views.EmpleadoDetailView.as_view(),
            name='empleado_detail'),

    path('update-empleados/<pk>/', 
            views.EmpleadoUpdateView.as_view(),
            name='modificar_empleado'),

    path('add-empleado/',
            views.EmpleadoCreateView.as_view(),
            name='empleado-add'),
    path(
        'success/',
         views.succesview.as_view(),
         name='correcto'),

    path(
        'delete-empleado/<pk>/',
         views.EmpleadoDeleteView.as_view(),
         name='eliminar-empleado'),
]
