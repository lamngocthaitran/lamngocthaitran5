# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:37:15 2024

@author: hs
"""

x=float(input("nhập giá trị thuộc [-89.9;88.8]"))
if -89.9<=x<=88.8:
    print("giá trị hợp lệ")
while x<-89.9 or x>88.8:
    x=float(input("nhập lại x="))
print("giá trị đã nhập là: ", x)
   