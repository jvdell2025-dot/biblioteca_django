# Biblioteca Django

Proyecto de la Práctica Semana 17.

Sistema CRUD hecho con Django con tres modelos relacionados:
- Categoria
- Autor
- Libro (relacionado con Autor y Categoria)

Incluye formularios de Django y CSS básico en las templates.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   git clone https://github.com/EL_USUARIO/biblioteca_django.git
   cd biblioteca_django

2. Crear y activar el entorno virtual:
   python -m venv venv
   
   venv\Scripts\activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Crear la base de datos:
   python manage.py migrate

5. Ejecutar el servidor:
   python manage.py runserver

6. Abrir http://127.0.0.1:8000/

Autor: JOSUE RAFAEL ESCAMILLA VENTURA