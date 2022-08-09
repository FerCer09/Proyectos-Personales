"""
Fernando Cervantes Joaquin
matricula: 1416339f
Es un Automata de pila que reconce las cadenas que la diferencia
#a's - #b's es congruente con 1 módulo 3, siempre y cuando la 
#a's son mayor que #b's

Las cadenas que se quieren reconocer estan en el archivo
'palabras.txt', modifique el archivo y escriba las cadenas

En la salida saldrá la cadena que leyó y un string diciendo
si el automata de pila reconoció o no reconoció la cadena 

Use el IDE Spyder para ejecutar el codigo, con los archivos en
el mismo directorio
"""

with open('reglas.txt','r') as f:
    reglas = [regla.split() for regla in f]        

with open('palabras.txt','r') as f2:
    cadenas = [cadena.split() for cadena in f2]

#Leo cadena por cadena del archivo palabras.txt    
for cadena in cadenas:
    letra=[]    #inicializo letra
    Estado='0'  #estado inicial cero
    pila=[]     #pila vacia
    continua = 1 # controla un ciclo     
    cumple_reglas='true'
    if(len(cadena) != 0 ):
        letra=list(cadena[0]) #obtengo la primera posicion de la lista cadena
        print('cadena: '+ cadena[0])
    else:
        print('Cadena: ')
    while continua != -1 :
        if(len(letra) == 0): #si ya me consumí toda la cadena
            car_leido = 'e'
        else:
            car_leido=letra.pop(0) #saco y obtengo el primer elemento
            
        for regla in reglas:
            existe=0
            if( str(Estado) == regla[0] and car_leido == regla[1]): #verifico si existe la regla
                if(regla[2] != 'e'):   #si me pide que saque de la pila 
                    if(len(pila) != 0):  # si la pila no esta vacia
                        if(pila.pop() != regla[2]): #si no es igual a lo que pide la regla
                            cumple_reglas='false'
                            break
                            break
                    else:
                        cumple_reglas='false'# si esta vacia, no lo reconocé
                        break
                        break
                Estado = regla[3] 
                if(regla[4] != 'e'): # si pido que inserte a la pila
                    pila.append(regla[4])
                existe=1    #Si Existío la regla
                break
        #me ayuda a romper el ciclo    
        if(car_leido == 'e'):   
            if(existe == 0):    ## si no existe la regla
                continua = -1
            if(cumple_reglas == 'false'):
                continua = -1
            elif(cumple_reglas == 'true' and len(pila) == 0): ##para salir en caso de que reconocio la cadena
                continua = -1

    if((Estado == '2') and cumple_reglas == 'true' and len(pila) == 0):
        print('Si se reconoció la cadena\n')     
    else:
        print('No se reconocio la cadena\n')  
      
        