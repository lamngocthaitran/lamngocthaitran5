# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:00:39 2024

@author: hs
"""

n=int(input("nhập số nguyên dương n :"))
tong=0
while n<=0:
    n=int(input("nhập lại số nguyên dương "))
for i in range(1,n+1):
    tu=1
    mau=i
    tong+=tu/mau
print(tong)
    
    