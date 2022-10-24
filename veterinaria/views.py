from django.shortcuts import render
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
                return redirect('tareas')
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

def tareas(request):
    return render(request, 'tareas.html')

