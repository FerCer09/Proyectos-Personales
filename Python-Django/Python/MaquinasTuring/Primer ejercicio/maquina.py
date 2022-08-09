'''
Autor: Fernando Cervantes Joaquin
Materia: Teoria de la computación
'''
with open('reglas.txt','r') as f:
    reglas = [regla.split() for regla in f]        

with open('palabras.txt','r') as f2:
    cadenas = [cadena.split() for cadena in f2]

# regla[0] estado actual
# regla[1] letra que espero
# regla[2] lo que escribo en la banda
# regla[3] direccion, d es derecha y i es izquierda
# regla[0] estado a donde iré
   
entrada = []
for i in range (100):
    entrada.append('#')
cadena = cadenas[0]
i = 1
for letra in cadena[0]:
    entrada[i] = letra
    i = i +1

estado = 0
ap = 0

while ap < len(entrada)-1:
    if(estado == 99):
        break
    for regla in reglas:
        car_leido = entrada[ap]
        if( str(estado) == regla[0] and car_leido == regla[1]):
            entrada[ap] = regla[2]
            if( regla[3] == 'd' ):
                ap = ap + 1
            else:
                ap = ap - 1
            # vamos al siguiente estado
            estado = int(regla[4])


if(estado == 100):
    print('Aceptado')
else:
    print('Rechazado')

'''
for letra in entrada:
    if (letra != '#'):
        print(letra, end = "")
    else:
        print(" ",end="")    
'''
print("\n")
print("Ultima configuración")
print("Estado = ", end ="") 
print(estado)
print("Ultima letra leida = ", end ="") 
print(car_leido)
print("Ultimo caracter puesto en la banda = ", end ="") 
print(entrada[ap])

  