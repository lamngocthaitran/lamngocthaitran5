# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:34:05 2024

@author: hs
"""


a=int(input("nhập số nguyên thứ 1: "))
b=int(input("nhập số nguyên thứ 2: "))
c=int(input("nhập số nguyên thứ 3: "))
d=int(input("nhập số nguyên thứ 4: "))
e=int(input("nhập số nguyên thứ 5: "))
def trungvi(a,b,c,d,e):
    so=[a,b,c,d,e]
    so.sort()
    return so[2]
print("trung vi la:", trungvi(a,b,c,d,e))