from django.contrib import admin
from .models import Dueno, Mascota, Atencion, Funcionario

# Register your models here.

admin.site.register(Dueno)
admin.site.register(Mascota)
admin.site.register(Atencion)
admin.site.register(Funcionario)


