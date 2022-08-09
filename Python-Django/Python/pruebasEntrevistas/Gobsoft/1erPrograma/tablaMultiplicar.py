import os
while (True):
    num = int(input ("Introduce un número del 1 al 10: "))
    if(num >= 1 and num <=10):
        break
    else:
        print("El número introducido no esta en entre el 1 y 10")

nombreArchivo = "tabla-"+str(num)+".txt"
file = open(nombreArchivo, "w")

i = 1
while(i <= 10):
    #realizando las multiplicaciones
    op = num * i
    file.write(str(num) + " x " + str(i) + " = " + str(op)+"\n")
    i += 1
file.close()

print("Programa terminado")

