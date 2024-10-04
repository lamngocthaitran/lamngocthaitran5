# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:03:05 2024

@author: hs
"""

n=int(input("nhập một số nguyên: "))
tong=1
for i in range(1,n+1):
    tong *=i
print("kết quả của",n,"! là: ",tong)