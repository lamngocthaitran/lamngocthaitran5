# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:14:47 2024

@author: hs
"""

import random
n=random.randint(20,30)
random_list=[]
for _ in range(n):
    random_list.append(random.randint(20,30))
print(f"số lượng phần tử là: {n}")
print("danh sách số ngẫu nhiên")
print(random_list)
