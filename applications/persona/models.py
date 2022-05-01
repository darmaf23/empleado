from os import F_OK
from django.db import models
from applications.departamento.models import Departamento

# Create your models here.
class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTROS'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    job =models.CharField('trabajo',max_length=50,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
 
    def __str__(self):
        return str(self.id)+ '-'+ self.first_name+ '-' + self.last_name