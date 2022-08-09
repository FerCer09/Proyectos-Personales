from django.urls import path
from . import views
app_name = 'materias'
urlpatterns = [
    path('', views.index, name='index'), 
    path('add/', views.add, name='add'),
    path('edit/<int:materia_id>/', views.edit, name='edit'),
    path('delete/<int:materia_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:materia_id>/', views.update, name='update'),

    path('enlazarAlumno/<int:id_materia>/<int:id_alumno>/', views.insertarMateriaAlumno, name='enlazarAlumnos'),
    path('agregarAlumno/<int:materia_id>/', views.listarAlumnos, name='listarAlumnos'),
    path('deleteAlumno/<int:id_alumno>/<int:id_materia>/', views.deleteAlumno, name='deleteAlumno'),
    path('MateriaAlumnos/<int:id_materia>/', views.obtenerAlumnosInscritos, name='materiaAlumnos'),
]