# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
num = int(input('Введите длину массива: '))
min_num = int(input('Введите минимальное число: '))
max_num = int(input('Введите максимальное число: '))
lst = []
for i in range(num+1):
    i = random.randint(1,10)
    lst.append(i)
print(lst)
for i in range(len(lst)):
    if min_num <= lst[i] <= max_num:
        print(f'Число из диапазона равно {lst[i]}. Индекс числа - {i}')