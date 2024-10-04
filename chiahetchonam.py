# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:05:06 2024

@author: hs
"""

n=[]
for i in range(2018,2829):
    if i %2==0 and i %5==0:
        n.append(i)
print("danh sách giá trị chẵn nguyên và chia hết cho 5 là: ", )
print(n)