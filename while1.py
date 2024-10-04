# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:16:47 2024

@author: hs
"""

x=float(input("nhập giá trị thuộc [-99;99]"))
if -99<=x<=99:
    print("Số bạn nhập hợp lệ")
while x<-99 or x>99:
    x=float(input("nhập lại x="))
print("giá trị đã nhập: ",x)
