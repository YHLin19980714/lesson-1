#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:34:18 2021

@author: fennieliang
"""

def max(a,b,c):
    if a>b:
        big = a
    else:
        big = b
    return c if big<c else big

max_number = max(500,300,100)

print (max_number)
        
    