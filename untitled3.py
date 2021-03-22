# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:41:33 2021

@author: MyPC
"""
x = int(input('enter a value '))
y = int(input('enter next value '))
z = int(input('multiples of number '))
for i in range(x,y+1):
    if z > (y+1):
        print('please enter numbers with in the range')
        break
    if i%z ==0:
        print(i)
        