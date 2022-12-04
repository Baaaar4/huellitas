from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.utils import timezone
#from contrib.django.models import User


# Create your models here.


class Dueno(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)



class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.CharField(max_length=2)
    patologias = models.TextField(blank=True)
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE)

    # def __str__(self, Dueno):
        # return self.nombre_m 


class Atencion(models.Model):
    descripcion = models.TextField(blank=True)
    medicamentos = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    peluqueria = models.BooleanField(default=False)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)	

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, primary_key=True)
    cargo = models.CharField(max_length=50)
   



 