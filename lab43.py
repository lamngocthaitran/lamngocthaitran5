# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:24:18 2024

@author: hs
"""

n=int(input("nhập một số nguyên: "))
if n<=0:
    print("vui lòng nhập số nguyên")
else:
    S=0
    for i in range(2,n+1):
        S+=i/i+1
    print(f"tong S là {round(S,3)}")