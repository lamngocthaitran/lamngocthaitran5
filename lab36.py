# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:47:18 2024

@author: hs
"""

n=int(input("nhập số nguyên :"))
tong=0
for i in range(1,n+1):
    tong+=i**2
print("tổng là=", tong)