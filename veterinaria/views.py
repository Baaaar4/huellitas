from django.shortcuts import render, redirect
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import * 
from .models import *


# Create your views h   ere.
def home(request):
    return render(request, 'home.html')

def servicios(request):
    return render(request, 'servicios.html')

def agendarcita(request):
    return render(request, 'agendarcita.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tarea')
            except:
                return render(request, 'login.html', {
                'form': UserCreationForm,
                'error': 'El Usuario ya existe'
                })
        return render(request, 'login.html', {
            'form': UserCreationForm,
            'error': 'El Usuario ya existe'
            })


def perfil(request):
    return render(request, 'perfil.html')

def mascota(request):
    mascota = Mascota.objects.filter(user=request.user)
    return render(request, 'mascota.html', {'mascota': mascota})

def nueva_atencion(request):
    if request.method == 'GET':
        return render(request, 'nueva_atencion.html', {
        'form': AtenForm
    })
    else:
        try:
            AtenForm(request.POST)
            new_atn = form.save(commit=False)
            new_atn.user =request.user
            new_atn.save()
            return redirect('mascota')
        except:
            return render(request, 'nueva_atencion.html', {
            'form': AtenForm,
            'error': 'Ingrese datos válidos'
            })

def header(request):
    return render(request, 'header.html')

def cerrar(request):
    logout(request)
    return redirect ('')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'El usuario o la contraseña son incorrectas'
        })
        else:
            login(request, user)
            return redirect('tarea')    


