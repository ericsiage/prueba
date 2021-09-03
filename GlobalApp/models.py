from django import db
from django.db import models




# Create your models here.

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=10)
    status=models.BooleanField(default=None)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    empresa=models.ForeignKey('Empresa', on_delete=models.CASCADE)
    price=models.IntegerField()
    fecha=models.DateField()
    choicesTransacciones=[(False,'closed'),(None,'pending'),(True,'reversed')]
    estatus_Transaccion=models.BooleanField(default=None,choices=choicesTransacciones, verbose_name="Status de transaccion")
    choicesAprobacion=[(False,'false'),(True,'true')]
    estatus_Aprobacion=models.BooleanField(default=None,choices=choicesAprobacion, verbose_name="Status de aprobacion")
    cobroFinal=models.BooleanField(
            verbose_name="Cobro Final")
        
    class Meta: 
        verbose_name='transaccion'
        verbose_name_plural='transacciones' 

    def __str__(self):
        return self.empresa.nombre


