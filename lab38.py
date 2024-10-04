# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:36:47 2024

@author: hs
"""

n=int(input("nhập số lẻ nguyên: "))
if n<=0 or n%2==0:
    print("vui lòng nhập một số lẻ")
else:
    S=1
    for i in range(1,n+1):
        S *=i
    print(S)
    