from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')    #verbose_name: tiene el titulo de ese campo para informar al usuario como se llama el campo
    imagen = models.ImageField(upload_to = 'imagenes/', verbose_name='Imagen', null =True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)

    def __str__(self):
        fila = "Título: "+ self.titulo + " - " + "Descripción: " + self.descripcion #es un string que puede ver el administrador
        return fila
    
    def delete(self, using=None, keep_parents=False): #para borrar la imagen despues de eliminar el registro
        self.imagen.storage.delete(self.imagen.name) #accede al almacenamiento fisico de la imagen y borralo
        super().delete()        #alteramos el adminitrador