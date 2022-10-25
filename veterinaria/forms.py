from django.forms import ModelForm
from .models import Atenciones

class AtenForm(ModelForm):
    class Meta:
        model = Atenciones
        fields = ['descripcion', 'peluqueria', 'medicamentos']