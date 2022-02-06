# Задание 1. Напишите программу заполнения списка положительными  и отрицательными элементами.

len_list1 = int(input('Введите длинну списка -->  '))
list1 = []
list2 = []

for i in range (len_list1):
    a = int(input('Введите элемент списка  '))
    list1.append(a)
    if a > 0:
        list2.append(a)
    i += 1

print(list1)
print(list2)
list3 = list1  # Копия списка для манипуляций.

# Найти наибольший элемент в списке
list3.sort(reverse=False)
print(list1[-1])

# Задание 2.  Дан список целых чисел, число k и значение С. Необходимо вставить на позицию с индексом k значение С, сдвинув все элементы.

len_list1 = int(input('Введите длинну списка -->  '))
list1 = []

for i in range(len_list1):
    a = int(input('Введите элемент списка  '))
    list1.append(a)

k = 1000000000000000
while k > len_list1:
    k = int(input('Введите индекс  '))
else:
    print()

aaa = int(input('Введите значение для вставки  '))

list1.insert(k, aaa)
print(list1)

# Задание 3. Заполнить список из 10 элементов случайными числами. Все положительные в начало списка.

n = int(input("Диапазон рандома: ,будут числа < "))
k = [0] * 10

for i in range(9):
    import random
    k[i] = random.randint(0, n-1)
print(k)
k.sort(reverse=True)
print(k)

# Задание 4. Написать программу , которая проверяет, находится ли введенное с клавиатуры число в списке.
# Список должен вводиться во время работы программы.

len_list4 = int(input('Введите длинну списка -->  '))
list4 = []

for i in range (len_list4):
    a4 = int(input('Введите элемент списка  '))
    list4.append(a4)

print(list4)
b4 = int(input('Введите число для проверки в списке  '))

for i in range (len_list4):
    if list4[i] == b4:
        print("Число присутствует в элементах списка")









