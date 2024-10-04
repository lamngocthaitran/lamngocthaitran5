# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:52:53 2024

@author: hs
"""

a = input("Nhập chuỗi: ")
print("Độ dài của chuỗi:", len(a))
special_chars = "!@#$%^&*()-=+./"
special_char_count = 0
lowercase_count = 0
uppercase_count = 0
digit_count = 0
for char in a:
    if char in special_chars:
        special_char_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
print("Số lượng ký tự đặc biệt:", special_char_count)
print("Số lượng ký tự chữ thường [a-z]:", lowercase_count)
print("Số lượng ký tự chữ số [0-9]:", digit_count)
print("Số lượng ký tự chữ hoa [A-Z]:", uppercase_count)
