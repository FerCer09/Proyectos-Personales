#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:32:42 2019

@author
"""
archivo = open("hello.txt","w")
archivo.write("hola como estas, estoy probando\nestas funciones\ncomo hacer")
archivo.close()

archivo = open("hello.txt","r")
mensaje= archivo.read()
print(mensaje)
archivo.close() 
print("\n")

archivo = open("hello.txt","r")
mensaje= archivo.readline()
print(mensaje)
archivo.close()

print("\n")

archivo = open("hello.txt","r")
mensaje= archivo.readlines() #lista de cadenas de todas las lineas del archivo
print(mensaje)
archivo.close()