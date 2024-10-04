# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:33:56 2024

@author: hs
"""

nam=int(input("nhập năm: "))
thang=int(input("nhập thang: "))
if thang in [1,3,5,7,8,10,12]:
    ngay=31
elif thang in [4,6,9,11]:
    ngay=30
else:
    if (nam%4 == 0 and nam %100 !=0) or (nam%400==0):
        ngay=29
        print("nam nhuan")
    else:
        ngay=28
        print("nam khong nhuan")
print(f"{ngay},{thang},{nam}")
