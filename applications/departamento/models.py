from django.db import models
from django.forms import BooleanField

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado',default=False)
    

    def __str__(self):
        return str(self.id) + '-' +self.name+ '-'+ self.shor_name


