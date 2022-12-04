from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import AtenForm, LoginForm 
from .models import Mascota, Atencion, Funcionario, Dueno
import datetime
from django.utils import timezone



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
                return redirect('mascota')
            except:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'El Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'El Usuario ya existe'
            })



def mascota(request):
    # Verificar que no exista la sesión
    if not request.session.has_key('username'):
    # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/signin')

    username = request.session['username']

    fecha=datetime.datetime.now()
    hora=fecha.hour

    mascota = Mascota.objects.all().order_by("id")
 
    
    context = {
        "username": username,
        "saludos":hora,
        "mascota" : mascota
    }

    return render(request, 'mascota.html', context=context)
 

def mascota_detail(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/signin')

    username = request.session['username']

    fecha=datetime.datetime.now()
    hora=fecha.hour
    

    if request.method == 'POST':
        form = AtenForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = username
            post.mascota = mascota
            post.publish_date = timezone.now()
            post.save()
            return redirect('mascota_detail', mascota.id)
    else:
        form = AtenForm()


    atencion = Atencion.objects.all().order_by("-publish_date")
    
    
    context = {
        "form": form,
        "username": username,
        "saludos":hora,
        "mascota": mascota,
        "atenciones" : atencion
    }
    
    return render(request, 'mascota_detail.html', context=context)

def atencion_edit(request, id_atencion):
    atencion = Atencion.objects.get(id=id_atencion)
    if request.method == 'GET':
        form = AtenForm(instance=atencion)
    else:
        form = AtenForm(request.POST, instance=atencion)
        if form.is_valid():
            form.save()
        return redirect('mascota')
    return render(request, 'atencion_edit.html',{'form':form} )

def atencion_delete(request, id_atencion):
    atencion = Atencion.objects.get(id=id_atencion)
    if request.method == 'POST':
        atencion.delete()
        return redirect('mascota')
    return render(request, 'atencion_delete.html',{'atencion':atencion} )


def header(request):
    return render(request, 'header.html')

def cerrar(request):
    logout(request)
    return redirect ('/')


def signin(request):
     # Verificar que no exista la sesión
    if request.session.has_key('username'):
        # Si la sesión existe, entonces me lleva al home
        return HttpResponseRedirect('/')
    else:
        # Si la sesión no existe, verifica el formulario
        if request.method == 'POST':
            # Si se recibe el formulario
            form = LoginForm(request.POST)
            if form.is_valid():
                # Si el formulario es válido, se verifican los datos
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                # Usa la función authenticate de django.contrib.auth
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Si los datos son válidos, crea la sesión
                    request.session['username'] = user.first_name or user.username
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                     return render(request, 'signin.html',{
                    'form': AuthenticationForm,
                    'error': 'El usuario o la contraseña son incorrectas'
        })

            
                    
        else:
            # Si no estamos recibiendo el formulario, entonces envíamos uno vacío
            form = LoginForm()
            #'error': 'El usuario o la contraseña son incorrectas'
            return render(request, 'signin.html', {'form': form })

    return render(request, 'signin.html', {'form': form})



