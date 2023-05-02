# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вывести один любой. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X
# *Пример:*
# 5
#     7 -2 3 5 1
#     6
#     -> 7

n = int(input('Введите количество элементов массива А: '))
import random
lst = [random.randint(0, 100) for i in range(n)]
print(lst)
x = int(input('Введите число Х: '))
min = abs(x - lst[0])
index = 0
for j in range (0, n):
    cnt = abs(x - lst[j])
    if cnt < min:
        min = cnt
        index = j
print ('В массиве А самый близкий по величине элемент к заданному числу Х это', lst[index]) 