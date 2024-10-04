# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:46:56 2024

@author: hs
"""

n=int(input("nhập số nguyên: "))
x=float(input("nhập x:" ))
tong=0
while n<=0:
    n=int(input("nhập số nguyên dương: "))
for i in range(1,n+1):
    tu=x**i
    mau=i+1
    tong+=tu/mau
print(tong)
    