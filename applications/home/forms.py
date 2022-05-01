from tkinter import Widget
from django import forms 
from  .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields =(
            'titulo',
            'subtitulo',
            'cantidad',
        )
        Widgets ={
            'titulo':forms.TextInput(
                attrs ={
                    'placeholder':'ingrese texto aqui',
                }
            )


        }

    def clean_cantidad(self):
        cantidad =self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese el erro mayor a 10')
        return cantidad

