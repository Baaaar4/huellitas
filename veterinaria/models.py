from django.db import models
from django.contrib.auth.models import User
from django import forms



# Create your models here.


class Dueno(models.Model):
    nombre_d = models.CharField(max_length=50)
    apellido_d = models.CharField(max_length=50)
    rut_d = models.CharField(max_length=9, primary_key=True)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100)
    user_d = models.ForeignKey(User, on_delete=models.RESTRICT)



class Mascota(models.Model):
    nombre_m = models.CharField(max_length=50)
    tipo_m = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    patologias = models.TextField(blank=True)
    dueno = models.ForeignKey('Dueno', on_delete=models.RESTRICT)

    def __str__(self, Dueno):
        return self.nombre_m 


class Atenciones(models.Model):
    descripcion = models.TextField(blank=True)
    medicamentos = models.TextField(blank=True)
    date = models.DateTimeField(null=True)
    peluqueria = models.BooleanField(default=False)
    mascota = models.ForeignKey('Mascota', on_delete=models.RESTRICT)	
    funcionario = models.ForeignKey('Funcionario', on_delete=models.RESTRICT)

   
    

class Funcionario(models.Model):
    nombre_f = models.CharField(max_length=50)
    apellido_f = models.CharField(max_length=50)
    rut_f = models.CharField(max_length=9, primary_key=True)
    user_f = models.ForeignKey(User, on_delete=models.RESTRICT)
   



 