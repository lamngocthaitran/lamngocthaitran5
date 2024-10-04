# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:10:43 2024

@author: hs
"""

n=int(input("nhập số nguyên dương: "))
tong=0
while n<=0:
    n=int(input("nhập lại số nguyên dương"))
for i in range(1,1+n):
    tong+=1/(2*i)
print(tong)