from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.


class Dueno(models.Model):
    nombre_d = models.CharField(max_length=20)
    apellido_d = models.CharField(max_length=20)
    rut_d = models.PositiveIntegerField(validators=[MinValueValidator(7), MaxValueValidator(8)])
    telefono = models.PositiveIntegerField(validators=[MinValueValidator(8), MaxValueValidator(9)])
    direccion = models.CharField(max_length=30)
    user_d = models.ForeignKey(User, on_delete=models.RESTRICT)



class Mascota(models.Model):
    nombre_m = models.CharField(max_length=20)
    raza = models.CharField(max_length=10)
    patologias = models.TextField(blank=True)
    dueno = models.ForeignKey('Dueno', on_delete=models.RESTRICT)


	

class Atenciones(models.Model):
    descripcion = models.TextField(blank=True)
    medicamentos = models.TextField(blank=True)
    date = models.DateTimeField(null=True)
    peluqueria = models.BooleanField(default=False)
    mascota = models.ForeignKey('Mascota', on_delete=models.RESTRICT)	
    funcionario = models.ForeignKey('Funcionario', on_delete=models.RESTRICT)

    

class Funcionario(models.Model):
    nombre_f = models.CharField(max_length=20)
    apellido_f = models.CharField(max_length=20)
    rut_f = models.PositiveIntegerField(validators=[MinValueValidator(7), MaxValueValidator(8)])
    user_f = models.ForeignKey(User, on_delete=models.RESTRICT)
    cargo = models.ForeignKey('Cargo', on_delete=models.RESTRICT)



    
class Cargo(models.Model):
    nombre_c = models.CharField(max_length=10)
    descripcion_c = models.TextField(blank=True)

 