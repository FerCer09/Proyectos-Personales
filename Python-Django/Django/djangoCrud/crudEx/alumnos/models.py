from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length=40)

class Maestros(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length=40)
    numTelefono =  models.CharField (max_length=12)
    direccion = models.CharField(max_length=50)

class Materias(models.Model):
    nombre = models.CharField(max_length = 20)
    horario = models.CharField(max_length=20)
    id_alumno = models.ManyToManyField(Alumnos)
    id_maestros = models.ManyToManyField(Maestros)

    def setIdAlumno(id):
        id_alumno = id
