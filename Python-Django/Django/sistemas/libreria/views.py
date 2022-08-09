from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro       #estoy importando el modelo Libro
from .forms import LibroForm    #importando el formulario
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')     #esta buscando un archivo nosotros.html


def libros(request):
    libros = Libro.objects.all()        #obtenemos todos los registros de libro
    context = {'libros':libros}
    return render(request, 'libros/index.html', context)     #le enviamos la variable 'libros' del objeto libros

def crearLibro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)        #identifica los elementos a traves del formulario
    context = {'formulario':formulario}
    if(formulario.is_valid()):
        formulario.save()               #guardando los datos introducidos
        return redirect('libros')       #redireccionando
    return render(request, 'libros/crear.html',context)     

def editarLibro(request, id):
    libro = Libro.objects.get(id = id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)     #Recuperando la información del libro
    context = {'formulario':formulario}
    if(formulario.is_valid() and request.POST):
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', context)  

def eliminarLibro(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    return redirect('libros')