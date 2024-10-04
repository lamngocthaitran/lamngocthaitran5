# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:15:27 2024

@author: ADMIN
"""

n=int(input("nhập một số nguyên: "))
if n<=0:
    print("vui lòng nhập số nguyên")
else:
    S=0
    for i in range(1,n+1):
        S+=1/(2*i+1)
    print(f"tong S là {round(S,3)}")