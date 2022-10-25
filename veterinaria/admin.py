from django.contrib import admin
from .models import Dueno, Mascota, Atenciones, Funcionario, Cargo

# Register your models here.

admin.site.register(Dueno)
admin.site.register(Mascota)
admin.site.register(Atenciones)
admin.site.register(Funcionario)
admin.site.register(Cargo)


