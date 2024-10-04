# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:27:23 2024

@author: hs
"""

n=int(input("nhập một số nguyên: "))
tong=0
while n<=0:
    n=int(input("nhập lại số nguyên "))
for i in range(2,n+1):
    tu=2*i+1
    mau=2*i+2
    tong+=tu/mau
print(tong)