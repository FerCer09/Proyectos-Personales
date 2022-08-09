import math
###########################varaiables######################################################
Grafo_archivo= "Grafo.txt";
Grafo_lista=[];
Matriz_adyacencia=[];
contador=0;

#Funcion que lee el grafo del archivo.
def lectura_grafo():
    Grafo = open(Grafo_archivo,'r');
    for linea in Grafo:#Se carga el grafo en una lista.
        linea=linea[:-1];#Se elimina el salto de linea.
        linea=linea.replace(' ','');#Se quitan los espacios
        Grafo_lista.append(list(linea));#Se añade a la lista
    Grafo_lista.pop();#S quita el elemento del final del archivo.
    h=0;
    for a in Grafo_lista:#Ciclo que reconstruye el grafo elmina elementos basura
        if(len(a) > 3):#Condicion para listas que tengan elementos basura
            longitud=3;
            while(longitud <= len(Grafo_lista[h])-1):#Ciclo que elemina los elementnos basura
                Grafo_lista[h][2]+=a[longitud];#Concate los ultimos elementos
                longitud+=1;
            Grafo_lista[h]=Grafo_lista[h][:(2-(len(Grafo_lista[h])-1))];#Borrar ls ultimos elementnos.
        h+=1;
#Funcion que obtiene un contador para saber la cantidad de columnas y filas.
def Obtener_contador():
    numero=0;
    contador=0;
    for a in Grafo_lista:
        if(numero != a[0]):
            numero=a[0];
            contador+=1;
    return contador;
#Funcion en donde se crea la matriz de ayacencia vacia
def crear_matriz_adyacencia():
    for fila in range (len(Grafo_lista)):
        Matriz_adyacencia.append([math.inf]*len(Grafo_lista));
#Funcion donde se llena la matriz
def llenar_matriz_adyacencia(contador):
    for linea in Grafo_lista:
        Matriz_adyacencia[(int(linea[0]))-1][(int(linea[1]))-1]=int(linea[2]);
    for i in range (len(Grafo_lista)-contador):#Limpia la mtriz de basura
        Matriz_adyacencia.pop();
    i=0;
    while(i<contador):
        Matriz_adyacencia[i]=Matriz_adyacencia[i][:contador-(len(Grafo_lista))];
        i+=1;

############################################Funcion principal##############################
        
lectura_grafo();##Se lee el grafo.
contador=Obtener_contador();
crear_matriz_adyacencia();
llenar_matriz_adyacencia(contador);
fila=0;
columna=0;
while(fila < contador):
    columna=0
    while(columna < contador):
        print (str(Matriz_adyacencia[fila][columna])+" ",end="")
        columna+=1;
    print("");
    fila+=1;
    