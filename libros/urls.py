from django.urls import path
from . import views

urlpatterns = [
    # Libros (página principal)
    path('', views.LibroList.as_view(), name='libro_list'),
    path('libros/nuevo/', views.LibroCreate.as_view(), name='libro_create'),
    path('libros/<int:pk>/editar/', views.LibroUpdate.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDelete.as_view(), name='libro_delete'),

    # Autores
    path('autores/', views.AutorList.as_view(), name='autor_list'),
    path('autores/nuevo/', views.AutorCreate.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', views.AutorUpdate.as_view(), name='autor_update'),
    path('autores/<int:pk>/eliminar/', views.AutorDelete.as_view(), name='autor_delete'),

    # Categorías
    path('categorias/', views.CategoriaList.as_view(), name='categoria_list'),
    path('categorias/nueva/', views.CategoriaCreate.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdate.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDelete.as_view(), name='categoria_delete'),
]