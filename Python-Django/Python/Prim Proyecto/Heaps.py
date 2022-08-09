#minHeaps
import math
def padre(lista,elemento):
    i=lista.index(elemento)-1 #para cumplir propiedad
    ipadre = int(i/2) #piso
    return int(lista[ipadre])

def hijoizq(lista,elemento):
    i=2*lista.index(elemento)+1
    if(i <= (len(lista)-1)):
        return str(lista[i])
    else:
        return -1
def hijoder(lista,elemento):
    i=2*lista.index(elemento)+1+1
    if(i <= (len(lista)-1)):
        return str(lista[i]) 
    else:
        return -1
def insertarH(lista,elemento):
    lista.append(elemento)
    bubble_up(lista,elemento)
    
def  bubble_up(lista,elemento):
    if(padre(lista,elemento)<=elemento):
        return 0
    else:
        #obtengo indices
        pa = lista.index(padre(lista,elemento))
        hij = lista.index(elemento)
        #intercambio
        aux=lista[pa]
        lista[pa] = elemento
        lista[hij] = aux
        bubble_up(lista,elemento)
        
def delete_min(lista):
    aux = lista[0]
    lista[0]=lista[len(lista)-1]
    lista[len(lista)-1]=aux
    minimo = lista.pop()
    bubble_down(lista,lista[0])
    return minimo

def bubble_down(lista,elemento):
    pa=lista.index(elemento)
    der=int(hijoder(lista,elemento))
    izq=int(hijoizq(lista,elemento))
    if(der == -1):  #si no tiene hijo derecho
        der = math.inf
    if(izq == -1):  #si no tiene hijo izquierdo
        izq = math.inf

    if(der >= elemento and izq >= elemento):
        return 0
    else:
        if(izq < der):
            hij=lista.index(izq)
            aux=lista[pa]
            lista[pa]=lista[hij]
            lista[hij]=aux
            bubble_down(lista,lista[hij])
        else:
            hij=lista.index(der)
            aux=lista[pa]
            lista[pa]=lista[hij]
            lista[hij]=aux
            bubble_down(lista,lista[hij])
    
lista= [1,2,3]
insertarH(lista,8)
insertarH(lista,9)
insertarH(lista,10)
insertarH(lista,11)
insertarH(lista,5)
insertarH(lista,4)
insertarH(lista,7)


print(lista)
print(padre(lista,5))
print(hijoder(lista,1))
print(delete_min(lista))
print(lista)
print(delete_min(lista))
print(lista)
print(delete_min(lista))
print(lista)
print(delete_min(lista))
print(lista)