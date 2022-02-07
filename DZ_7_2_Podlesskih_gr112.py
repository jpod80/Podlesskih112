# Задание 1. Нахождение минимального элемента главной диагонали.
import random as r
import math

size_array = int(input('Размерность массива -->  '))
all_array = [[r.randint(1, 100) for col in range(size_array)] for row in range(size_array)]
diagonal = []

for row in all_array:
    for col in row:
        print(col, end="\t")
    print()

for i in range(size_array):
    diagonal.append(all_array[i][i])
print("Диагональ", diagonal)

diagonal_min = int
diagonal_min = min(diagonal)
print("Минимальный элемент в диагонали", diagonal_min)
print()


# Задание 2. Нужно нечетные строки двумерного списка заменить на одномерный список.
import random as r
import math

size_array2 = 6
all_array2 = [[r.randint(1, 10) for col in range(size_array2)] for row in range(size_array2)]
list2 = [r.randint(1, 10) for l in range(size_array2)]

for row in all_array2:
    for col in row:
        print(col, end="\t")
    print()

print(list2)

for row in range(len(all_array2)):
    if row % 2 == 0:
        for col in range(len(all_array2[row])):
            print(list2[col], end="\t")
        print()
        for col in range(len(all_array2[row])):
            print(all_array2[row+1][col], end="\t")
        print()
