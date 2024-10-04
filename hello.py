# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:49:24 2024

@author: hs
"""

n=int(input("nhập số lần muốn in từ hello:"))
if 0<n<1000:
    for i in range(n):
        print("Hello")
else:
    print("số lần in không hợp lệ. Vui lòng nhập số nhỏ hơn")