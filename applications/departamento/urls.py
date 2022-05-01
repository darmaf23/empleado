from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
     path(
        'departamento-lista/',
         views.DepartamentoListView.as_view(),
         name='departamento-list'),


 ]
