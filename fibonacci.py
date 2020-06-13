# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:56:28 2020

@author: Ishika Garg
"""

x=int(input())
a=0
s=1
if x<=0:
    print(a)
else:
    print(a,s,end=" ")
    for i in range(2,x):
        f=a+s
        print(f,end=" ")
        a=s
        s=f