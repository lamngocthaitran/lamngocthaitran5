# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:35:14 2024

@author: hs
"""


numbers = [0] * ((3838 - 2020) // 2 + 1)  
for i in range(2020, 3839):
    if i % 2 == 0:
        numbers[id] = i
        id += 1
chia_9 = [0] * (id)  
id_9 = 0
for num in numbers:
    if num != 0 and num % 9 == 0:  
        chia_9[id_9] = num
        id_9 += 1
for i in range(id_9):
    if i == id_9 - 1:
        print(chia_9[i], end='')  
    else:
        print(chia_9[i], end='\t')  