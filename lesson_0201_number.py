# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 16:03:37 2021

@author: fennieliang
"""
#manually create an anaconda Virtual Environment:
    #    conda create -n NLP
    #    conda activate NLP
    #    deactivate a VM: at current vm type "conda deactivate"
    #    remove a VM: conda env remove -n NLP
    #practice: create a new VM called test and see what happens aftward

#Integer
a=1;b=2
print (f'1. a + b = {a+b}')
#在字串裡面進行計算，前面要用一個f，代表format，後面再加大括號
#這樣大括號內的變數才會變成variable，而不是字串
#print ("\n")

#Float
a=38.5  
print (f'2. a + b = {a+b}')
#print ("\n")

b=1e+3 
#1e means 1*10^, le+3 means 1*10^(+3) and so on 
print (f"3. b = {b}")#because b is a float, the result needs to be 1000.0 not 1000
#print ("\n")

print (f"4. a + b = {a+b}") 
#print ("\n")
sum=a+b
print (f"5. a + b = {sum}") 


sum = int(a+b)
print ("the result is ", sum) #This is an old version of printing results 
#print ("\n")

'''
#practice 0201 take two input integers and print the sum up result

'''
aaa=input()


'''
#practice 0202 take input number for 5 times and print the result
  
'''  
 
'''
#practice 0203 print a 20 layers of a * triangle
  
''' 