# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:19:16 2024

@author: hs
"""

n=int(input("nhập một số nguyên: "))
tong=0
while n<=0:
    n=int(input("nhập lại số nguyên"))
for i in range(1,n+1):
    tu=1
    mau=i*(i+1)
    tong+= tu/mau
print(tong)
