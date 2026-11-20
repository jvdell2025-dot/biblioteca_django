from django import forms
from .models import Categoria, Autor, Libro

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'