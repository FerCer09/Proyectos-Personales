from xml.dom.minidom import Document
from django.urls import path
from . import views

#para poder ver las imagenes se agregan las siguientes librerias
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [  #Permite acceder a la vista (views.py)
    path('',views.inicio, name = 'inicio'),     # '' signfica que si accede a la raiz, accede a la función inicio del archivo views, name='inicio' nos ayuda acceder a la url por el nombre 'inicio'
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('libros', views.libros, name = 'libros'),
    path('libros/crear', views.crearLibro, name = 'crear_libro'),
    path('libros/editar', views.editarLibro, name = 'editarLibro'),
    path('eliminar/<int:id>', views.eliminarLibro, name = 'eliminarLibro'),
    path('libros/editar/<int:id>', views.editarLibro, name = 'editarLibro'),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)   #Agregar esto para ver las imagenes