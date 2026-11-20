from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Autor, Libro
from .forms import CategoriaForm, AutorForm, LibroForm

# ---------- CATEGORIA ----------
class CategoriaList(ListView):
    model = Categoria
    template_name = 'libros/categoria_list.html'

class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'libros/confirmar_eliminar.html'
    success_url = reverse_lazy('categoria_list')

# ---------- AUTOR ----------
class AutorList(ListView):
    model = Autor
    template_name = 'libros/autor_list.html'

class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('autor_list')

class AutorDelete(DeleteView):
    model = Autor
    template_name = 'libros/confirmar_eliminar.html'
    success_url = reverse_lazy('autor_list')

# ---------- LIBRO ----------
class LibroList(ListView):
    model = Libro
    template_name = 'libros/libro_list.html'

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('libro_list')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'libros/confirmar_eliminar.html'
    success_url = reverse_lazy('libro_list')