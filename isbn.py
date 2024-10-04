# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:44:08 2024

@author: ADMIN
"""

def tinhisbn(ma):
    tong=0
    for i in range(9):
        tong+=(10-i)*int(ma[i])
    chusokt=(11-tong%11)%11
    if chusokt==10:
        chusokt='X'
    print(ma + str(chusokt))
ma = input("nhập 9 chữ số: ")
tinhisbn(ma)