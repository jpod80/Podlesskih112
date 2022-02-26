# Задание 1. Даны 2 списка одинакоой длинны. Создать словарь.

a_list = ['red', 'green', 'blue']
b_list = ['#FF0000', '#008000', '#0000FF']
d_dict = dict(zip(a_list, b_list))
print(d_dict)

# Задание 2. Ключи - цифры 1...20. Значения эти же ключи в кубе.

a = {i: i**3 for i in range(1, 11)}
print(a)

# Задание 3. Используя 2 списка создай новый словарь используя генератор.

aaa_list = ['color', 'fruit', 'pet']
bbb_list = ['blue', 'apple', 'dog']
ccc_dict = {k: v for k, v in zip(aaa_list, bbb_list)}
print(ccc_dict)

# Задание 4. Функция нахождения минимального  значения произвольного количества аргументов

def min_number(list_n):
    min_n = min(list_n)
    return min_n

list_numbers = [10, 9]
list_numbers1 = [2, 3, 4]
list_numbers2 = [3, 5, 10, 6]
print(min_number(list_numbers2))

