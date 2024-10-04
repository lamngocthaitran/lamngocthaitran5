# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:18:19 2024

@author: ADMIN
"""

N = int(input("Nhập vào một số nguyên dương N: "))
tong = 0
while N > 0:
  chu_so = N % 10
  tong += chu_so
  N //= 10
print("Tổng các chữ số của", N, "là:", tong)