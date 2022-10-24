from django.shortcuts import render, redirect
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login



# Create your views here.
def home(request):
    return render(request, 'home.html')

def servicios(request):
    return render(request, 'servicios.html')

def agendarcita(request):
    return render(request, 'agendarcita.html')

def login(request):
    
    if request.method == 'GET':
        return render(request, 'login.html', {
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

def tarea(request):
    return render(request, 'tarea.html')

def header(request):
    return render(request, 'header.html')