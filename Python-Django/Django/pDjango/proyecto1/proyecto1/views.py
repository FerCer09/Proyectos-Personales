from datetime import datetime
from turtle import end_fill
from django.http import HttpResponse

def saludo(solicitud): #Caada función es una vista, esta es la primera vista
    documento = """<html>
                        <body>
                            <h1>Hola, esta es mi primera pagina con Django</h2>
                        </body>
                    </html>"""      #las triple comillas reconoce todo como una sola cadena
    return HttpResponse(documento)
    #Nos vamos a urls.py, para enlazar esta vista en una url

def despedida(solicitud):

    return HttpResponse("Hasta luego")

def otro(solicitud):

    return HttpResponse("Ete es otra vista")

def dameFecha(solicitud):
    fechaActual = datetime.now()      #utilizando un modulo de python

    var = "hola, este es una variable"
    documento = """<html>
                        <body>
                            <h1>Fecha y hora actuales %s</h2>   
                        </body>
                    </html>""" % fechaActual #%s es donde se va imprimir la fecha actual de la variable fechaActual
    return HttpResponse(documento)

#Django utilia url frienly

#función para pasar parametros por la ur

def calculaEdad (solicitud, year, edad):

    periodo = year - 2022
    edadFutura = edad + periodo
    documento = """<html>
                        <body>
                            <h2>En el año %s tendrás %s años</h2>   
                        </body>
                    </html>""" %(year, edadFutura)
    return HttpResponse(documento)
