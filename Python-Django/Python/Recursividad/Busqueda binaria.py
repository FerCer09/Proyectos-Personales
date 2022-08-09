#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 06:27:05 2019

@author: fernando
"""

def BSR(lista,st,en,x):
    if(st>en):
        return -1
    m = int((st+en)/2)
    if( lista[m] == x):
        return 1
    elif(lista[m]<x):
        return BSR(lista,m+1,en,x)
    else:
        return BSR(lista,st,m-1,x)
    
lista=[1,2,3,5,15,18,30,35]
Verdad = BSR(lista,0,len(lista),15)
if(Verdad == 1):
    print("Si esta")
else:
    print("No esta")