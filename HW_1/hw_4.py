# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

print('Сколько всего у нас журавликов?')
s = int(input())
a = 0
b = 0
if s % 2 == 0 or s == 6:
    a = s // 6
    b = s * 2 // 3
    print('Петя и Серёжа сделали по ', a , 'журавликов,' , 'Катя сделала' , b , 'журавликов.')
else:
    print('По условию задачи, количество журавликов чётное, не менее шести. Пожалуйста, перезапустите программу и повторите ввод.')