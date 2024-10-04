# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:47:29 2024

@author: hs
"""

n=int(input("nhập số chẵn nguyên:"))
if n<=0 or n%2!=0:
    print("nhập một số chẵn")
else:
    S=(2+n)*(n+2)/4
print("tổng S=",S)