# # Задание 1. Создать случайный список из 20 элементов. Посчитать сумму.
#
# # import random as r
# # mas1 = [r.randrange(10) for i in range(10)]
# # print(mas1)
#
# import math
# from random import randint
#
# numbers20 = []
# sum20 = 0
# for i in range(20):
#     numbers20.append(randint(0, 10))
#     sum20 += numbers20[i]
#
# #math Второй способ
# su = sum(numbers20)
#
# print(numbers20)
# print(sum20)
# print(sum20)

# # Задание 2. Транспонирование матрицы.
#
# ### ??? Почему не работает второй цикл без первого цикла?
# ### Выходит второй цикл неверно написан, если он не работает самостоятельно?
#
# mathrics1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# row = 0
# for row in mathrics1:
#     for col in row:
#         print(col, end="\t\t")
#     print()
#
# print()
# i = 0
# for col in row:
#     for row in mathrics1:
#         print(row[i], end="\t\t")
#     i += 1
#     print()

# Задание 3. Уникальные рандомные числа.

import random as r

numbers20 = []
sum20 = 0
for i in range(10):
    a = r.randint(0, 100)
    if a not in numbers20:
        numbers20.append(a)

print(numbers20)
