#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:50:28 2021

@author: fennieliang
"""

import practice_0204


class Lesson:

    teacher = 'Fennie' # variable shared within the class

    def __init__(self, firstname, lastname):
        self.firstname = firstname    # instance variable unique to each instance
        self.lastname = lastname
        
   
 
p=Lesson("John","Johnson")      
if __name__ == '__main__':
    
    print(Lesson.teacher)
    print (p.firstname)
    print (p.lastname)

