from django.forms import modelform_factory
from .models import *

class AtenForm(ModelForm):
    class Meta:
        model = Atenciones
        fields = ['description', 'peluqueria', 'medicamentos']