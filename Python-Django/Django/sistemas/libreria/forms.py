from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'      #todos los campos
        #fields = ['titulo','imagen']       este me permite seleccionar solo los campos que quiera