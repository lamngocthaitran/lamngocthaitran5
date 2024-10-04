# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:52:34 2024

@author: hs
"""

n=int(input("nhập số nguyên n: "))
while n<=0:
    n=int(input("vui lòng nhập lại số nguyên n"))
for i in range(1,n+1):
    if n%i==0:
        print("ước chung là của n là: ",i)
    