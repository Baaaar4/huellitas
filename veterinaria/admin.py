from django.contrib import admin
from .models import Dueno, Mascota, Atenciones, Funcionario

# Register your models here.

admin.site.register(Dueno)
admin.site.register(Mascota)
admin.site.register(Atenciones)
admin.site.register(Funcionario)


