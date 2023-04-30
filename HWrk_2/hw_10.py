# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.

import random
coins = int(input("Ведите количество монеток : "))
orel, reshka = 0, 0

for _ in range(coins):
    n = random.randint(0,1)
    if n == 0:
        orel+=1
    else:
        reshka+=1
if orel > reshka:
    print('На столе', orel, 'монет лежат орлом вверх. Осталось перевернуть', reshka, 'монет')
else:
    print('На столе', reshka, 'монет лежат решкой вверх. Осталось перевернуть', orel, 'монет')


