from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


'''class Dueno(models.Model):
	nombre_d = models.Charfield(max_length=20)
	apellido_d = models.Charfield(max_length=20)
	rut_d = models.PositiveIntegerField(max_length=9)
	telefono = models.PositiveIntegerField(max_length=9)
	direccion = models.Charfield(max_length=30)
	user = models.ForeignKey(User, on_delete=models.RESTRICT)

class Mascota(models.Model):
	nombre_m = models.Charfield(max_length=20)
	raza = models.Charfield(max_length=10)
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
	nombre_f = models.Charfield(max_length=20)
	apellido_f = models.Charfield(max_length=20)
	rut_f = models.PositiveIntegerField(max_length=9)
	user = models.ForeignKey(User)
	cargo = models.ForeignKey('Cargo', on_delete=models.RESTRICT)

class Cargo(models.Model):
	nombre_c = models.Charfield(max_length=10)'''
	