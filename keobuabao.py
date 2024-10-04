# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:08:10 2024

@author: ADMIN
"""

import random
soluong= random.randint(8, 20)
choices = ['Kéo', 'Búa', 'Bao']
players = [{'name': f"Người chơi {i + 1}", 'choice': None} for i in range(soluong)]
may = random.choice(choices)
print(f"Máy chọn: {may}\n")
for player in players:
    player['choice'] = random.choice(choices)
    if player['choice'] == may:
        result = "Hòa"
    elif (player['choice'] == 'Kéo' and may == 'Bao') or \
         (player['choice'] == 'Búa' and may == 'Kéo') or \
         (player['choice'] == 'Bao' and may == 'Búa'):
        result = "Thắng"
    else:
        result = "Thua"
    
    print(f"{player['name']} chọn {player['choice']} - {result}")