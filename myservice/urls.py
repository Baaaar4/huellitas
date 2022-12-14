"""myservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from veterinaria import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('servicios', views.servicios, name='servicios'),
    path('agendarcita', views.agendarcita, name='agendarcita'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('mascota', views.mascota, name='mascota'),
    path('detail/<int:id_mascota>/', views.mascota_detail, name='mascota_detail'),
    path('logout', views.cerrar, name='logout'),
    path('editar/<int:id_atencion>/', views.atencion_edit, name='atencion_edit'),
    path('eliminar/<int:id_atencion>/', views.atencion_delete, name='atencion_delete'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)