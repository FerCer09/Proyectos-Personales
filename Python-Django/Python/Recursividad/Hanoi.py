#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 05:44:35 2019

@author: fernando
"""
def torres_Hanoi(num,src,dst,temp ):
        if(num<1):
            return
        torres_Hanoi(num-1,src,temp,dst)
        print("Moviendo disco %s de "%num +str(src)+" a "+str(dst))
        torres_Hanoi(num-1,temp,dst,src)        

num =2
torres_Hanoi(num,'origen','Destino','aux')