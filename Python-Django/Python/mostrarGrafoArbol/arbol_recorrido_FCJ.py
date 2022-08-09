# Fernando Cervantes Joaquín

import time
from graphviz import Digraph
g = Digraph('G', filename='graphviz_Graph1.dot', format='png')

laberinto={"a":"inicio", "b":"inicio", "c":"inicio", "d":"inicio", "e":"a", "f":"a", "m":"e", "g":"b", "h":"b", "n":"h", "o":"n", "salida":"o", "p":"n", "i":"c", "j":"c", "k":"d", "l":"d"}

"""
El diccionario que creamos arriba son los elementos de nuestro arbol, en donde el primer elemento de la pareja es el hijo, y el segundo el padre, por ejemplo "a" es hijo de "inicio", si lo ponemos de forma grafica quedaria como se muestra a continuacion:

                     ---inicio---
                    /   \      /   \
                    a    b    c    d
                   / \  / \  / \  / \
                  e  f  g  h i  j k  l 
                 /          \    
                m            n
                            / \
                           o   p
                          /
                       salida
"""                
def rec_serc(inicio,meta):   
    ruta.append(inicio)
    if inicio==meta:
        return meta
    print(ruta)
    time.sleep(0.5)
    for j,k in laberinto.items():
        if k==inicio:
            busqueda=rec_serc(j,meta)
            if busqueda:
                return busqueda 
    ruta.pop()
    return 0

def crear_arbol_grafico():
	for j,k in laberinto.items():
		g.edge(k,j)

#	g.view()

def ruta_grafico():
	i = 0
	j = i + 1 
	while j < len(ruta):
		a = "["+ruta[i]+"]"
		b = "["+ruta[j]+"]"

		g.edge(a,b)
		j += 1
		i += 1

ruta=[]
var_inicio = "inicio"
var_fin = "salida"

crear_arbol_grafico()

busqueda=rec_serc(var_inicio,var_fin)
if busqueda:
    print("La ruta completa es: ", ruta)
	
else:
    print("No existe una ruta")

ruta_grafico()
g.view()

