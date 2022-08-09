def getElementsTrue(func, lista):
    elementsTrue = []
    numElement = 0
    numCondicion = int( input("Introduce el valor minimo que deben tener los valores de la lista: "))
    for iterNum in lista:
        if( func(numCondicion, iterNum) == True ):
            elementsTrue.append(iterNum)
        numElement +=1
    return elementsTrue

def condicionMayor(numCondicion,num):
    if num >= numCondicion:
        return True
    else:
        return False


def main():
    sizeList = int ( input ("Introduce el tamaño de la lista:") )
    listaEntrada = []
    i = 0
    while( i < sizeList):
        elementos = int ( input ("Introduce el elemento "+str(i) + " de la lista:" ))
        listaEntrada.append(elementos)
        i+=1
    
    
    listaSalida = []
    listaSalida = getElementsTrue(condicionMayor,listaEntrada)

    print("\nLa lista con los elementos mayores son: ", end="")
    print(listaSalida)
main() 