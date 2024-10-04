# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:24:45 2024

@author: hs
"""

n=int(input("nhập số nguyên: "))
if n<=1:
    print("không phải là số nguyên tố")
elif n==2:
    print("là số nguyên tố")
else:
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            print("không phải là số nguyên tố")
            break
    else:
        print("là số nguyên tố")
