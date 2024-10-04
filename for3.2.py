# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:07:06 2024

@author: hs
"""

import random
n=random.uniform(18,99)
squared_values=[]
for _ in range(n):
    squared_values.append(n**2)
print("danh sách giá trị bình phương của số thực ngẫu nhiên")
for value in squared_values:
    print(value)
