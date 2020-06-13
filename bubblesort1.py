# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:33:36 2020

@author: Ishika Garg

bubble sort algo
"""
def bs(a):
    b=len(a)-1
    for x in range (b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a
    
a=[32,5,3,6,7,54,87]
print(bs(a))