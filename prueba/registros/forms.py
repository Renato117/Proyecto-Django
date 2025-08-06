from django import forms
from .models import ComentarioContacto
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

<<<<<<< HEAD

=======
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

<<<<<<< HEAD
class FormArchivos (ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo', 'descripcion', 'archivo')
        widgets = {
            'archivo': CustomClearableFileInput
        }
=======
class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo', 'descripcion', 'archivo')
        widgets = { 'archivo': CustomClearableFileInput }
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
