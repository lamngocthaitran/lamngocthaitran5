# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:36:39 2024

@author: hs
"""

n=int(input("nhập số nguyên: "))
S=0
for i in range(1, n+1):
    S+=i
print("tổng các chữ số từ 1 đến",n,"là:", S )
