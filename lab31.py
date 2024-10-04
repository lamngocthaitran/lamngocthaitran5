# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:56:55 2024

@author: hs
"""

a=int(input("nhập số nguyên a: "))
b=int(input("nhập số nguyên b: "))
c=int(input("nhập số nguyên c: "))
if a<=0 or b<=0 or c<=0:
    print("ba số không lập được thành một tam giác")
if a+b>c or a+c>b or b+c>a:
    if a==b==c:
        print("là tam giác đều")
    elif a==b or a==c or b==c:
        print("là tam giác cân")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("là tam giác vuông")
    else:
        print("là tam giác thường")
else:
    print("không tạo thành 1 tam giác")
        
