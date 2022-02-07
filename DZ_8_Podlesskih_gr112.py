# Задание 1. Написать функции нахождения фигур.

def area_rectangle():
    rect_a = int(input("Основание фигуры --> " ))
    rect_b = int(input("Высота фигуры --> "))
    print("Площадь квадрата", rect_a * rect_b, " квадратных единиц")

def area_triangle():
    triang_a = int(input("Основание фигуры --> " ))
    nriang_b = int(input("Высота фигуры --> "))
    print("Площадь треугольника", 0.5 * triang_a * nriang_b, " квадратных единиц")

def area_circle():
    circle_radius = float(input("Радиус круга --> "))
    print("Площадь круга", 3.14159 * circle_radius * circle_radius, " квадратных единиц")
    #Не смог радиус возвести в квадрат, жалуется на тип данных.

a = int(input("Выберите фигуру: 1 - прям-к, 2 - тре-к, 3 - Круг --->  " ))
if a == 1:
    area_rectangle()
elif a == 2:
    area_triangle()
elif a == 3:
    area_circle()
else:
    print("Ошибка при выборе фигуры")


# Задание 2. Дан список целых чисел. Найти Мин среди простых чисел и Макс среди непростых чисел.

import math
def prime_numbers_separator(list1):
    list1 = []
    list1 = a
    list_prime = []
    i = 0
    for i in range(len(a)):
        for devider in range(2, list1[i]+1):
            if list1[i] % devider == 0:
                break
            else:
                list_prime.append(list1[i])
                break
    print(list_prime)
    print("Min: ", min(list_prime))
    print("Max: ", max(list_prime))


a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 17, 1]
prime_numbers_separator(a)  # Запуск функции

