"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto1.views import calculaEdad, dameFecha, despedida, otro, saludo      #llamamos la función o vista saludo del archivo views.py del proyecto

# enlaces de la urls con las vistas(funciones de views.py)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('adios/', despedida),
    path('otro/', otro),
    path('fecha/', dameFecha),
    path('edadFutura/<int:edad>/<int:year>', calculaEdad),         #Estoy indicando que en url estoy pasando un parametro tipo int
]


