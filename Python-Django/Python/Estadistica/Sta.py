#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:22:28 2019

@author: fernando
"""
lista=[19,20,22,18,17,17,21,19,22,20,23,24,16,25,22]
i=0
while( i<len(lista) ):
    j=0
    while( j<len(lista)-i):
        if(lista[j]>lista[j+1]):
               aux= lista[j]
               lista[j]=lista[j+1]
               lista[j+1]=aux
        j = j+1
    i= i+1
print(lista)