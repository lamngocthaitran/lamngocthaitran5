# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:08:54 2024

@author: hs
"""

import random

choices = ['keo', 'bua', 'bao']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Hoa"
    elif (user_choice == 'keo' and computer_choice == 'bao') or \
         (user_choice == 'bua' and computer_choice == 'keo') or \
         (user_choice == 'bao' and computer_choice == 'bua'):
        return "Nguoi thang"
    else:
        return "May thang"

def play_game():
   
    user_choice = input("Nhap su lua chon cua ban (keo, bua, bao): ").strip().lower()
    
    if user_choice not in choices:
        print("Lua chon khong hop le. Vui long nhap 'keo','bua','bao'.")
        return
    
    computer_choice = random.choice(choices)
    print(f"May ra: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(f"Ket qua: {result}")

if __name__ == "__main__":
    play_game()