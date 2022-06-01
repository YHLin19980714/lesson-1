#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:33:07 2021

@author: fennieliang
"""
import math

for i in range (20):#from 0-19

    if math.remainder(i, 2)!=0:#exclude even number
        for j in range (20-int(i/2)):#position the print in centre 
            print (" ", end='')#print spaces before * 
        for k in range (i):#control the number of * to be printed
            print ("*", end='')
        print ('')

#math.remainder(i, 2)  代表i/2的餘數
#!=      代表不等於
#end=''  代表結尾不換行，改加''
#i=17  
#(math.remainder(i, 10))
