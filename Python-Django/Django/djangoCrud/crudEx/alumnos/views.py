from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Alumnos, Materias
def index(request):
    materias = Materias.objects.all()
    context = {'materias': materias}
    return render(request, 'alumnos/index.html', context)
def add(request):
    return render(request, 'alumnos/add.html')
def insert(request):
    nombreMateria = request.POST.get('nombre_materia')
    horarioMateria = request.POST.get('horario')
    materia = Materias(nombre=nombreMateria, horario=horarioMateria)
    materia.save()
    return HttpResponseRedirect('/materias/')
def edit(request, materia_id):
    materia = get_object_or_404(Materias, pk=materia_id)
    context = {'materia': materia}
    return render(request, 'alumnos/edit.html', context)
def update(request, materia_id):
    materia = get_object_or_404(Materias, pk=materia_id)
    materia.horario = request.POST.get('horario')
    materia.save()
    return HttpResponseRedirect('/materias/')
def delete(request, materia_id):
    materia = get_object_or_404(Materias, pk=materia_id)
    materia.delete()
    return HttpResponseRedirect('/materias/')

def listarAlumnos(request, materia_id):
    materia = get_object_or_404(Materias, pk=materia_id)
    alumnos = Alumnos.objects.all()
    context = {'materia': materia, 'alumnos':alumnos}
    return render(request, 'alumnos/indexAlumnos.html', context)

def insertarMateriaAlumno(request, id_materia, id_alumno):
    materia = get_object_or_404(Materias, pk=id_materia)
    alumno = get_object_or_404(Alumnos, pk=id_alumno)    
    materia.id_alumno.add(alumno)
    return HttpResponseRedirect('/materias/')

def deleteAlumno(request, id_alumno, id_materia):
    alumno = Alumnos.objects.filter(materias = id_materia, id = id_alumno)
    alumno.delete()
    return HttpResponseRedirect('/materias/')

def obtenerAlumnosInscritos(request, id_materia):
    materia = get_object_or_404(Materias, pk=id_materia)
    alumnos = Alumnos.objects.filter(materias = id_materia)
    context = {'materia':materia,'alumnos': alumnos}
    return render(request, 'alumnos/indexMateriaAlumnos.html', context)




#def update(request, materia_id):
#    materia = get_object_or_404(Materias, pk=materia_id)
#    materia.horario = request.POST.get('horario')
#    materia.save()
#    return HttpResponseRedirect('/materias/')
