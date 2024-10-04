# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:15:14 2024

@author: hs
"""

danhsach=[]
min=979
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y +9*z == 979:
                sum=x+y+z
                if sum < min:
                    min=sum
                    danhsach=[(x,y,z)]
print(f"{danhsach} với bộ nghiệm (x+y+z)={min}")
    
    