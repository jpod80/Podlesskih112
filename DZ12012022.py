# # Group 112   DZ от 12.01.2022
# # Задание 1. Чередование символов по горизонтали.
#
# i = 1
# while i < 5:                            # Пустой столбец
#
#     j = 1
#     while j < 19:
#         if j % 2 == 0:                  # Наполнение строк с чередованием
#             print("-", end='')
#         else:
#             print("+", end='')
#         j += 1
#
#     print()                             # БЕЗ ПУСТОГО ПРИНТА НЕД ДВИЖЕНИЯ ВНИЗ!!!!
#     i += 1


# # Задание 2. Пользователь с клавиатуры вводит 2 числа. Необходимо указать все нечетные числа в диапазоне.
#
# a = int(input("Начало диапазона -->"))
# b = int(input("Конец диапазона -->"))
# # i = a
# while a < b + 1:
#     if a % 2 != 0:
#         print(a, end=" ")
#     else:
#         print("", end="")
#     a += 1


# Задание 3. Игра угадай число.

from random import randint
a = randint(1, 100)                               # Загадали случайное число
print("Вывод случайного целого числа ", a)

i = 0
attempt = 0
while i != a:
    i = int(input("Угадай число от 1 до 100 -->"))
    if i > a:
        print("Загаданное число меньше")
    elif i < a:
        print("Загаданное число больше")
    else:
        print("В точку")
    attempt += 1
print("Количество попыток", attempt)




