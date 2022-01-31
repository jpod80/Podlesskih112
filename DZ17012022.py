# # Задание 1. Выведите все элементы из списка с четными индексами.
#
# n = int(input("Количество чисел --> "))
# i = 0
# a = [0]*n
#
# for i in range(n):
#     a[i] = int(input("Заведите число --> "))
#
# for i in a:
#     if i % 2 != 0:
#         print(i, end=' ')

# # Задача 2. Выведите все элементы списка, которые больше предыдущего элемента.
#
# nn = int(input("Количество чисел --> "))
# i = 0
# aa = [0]*nn
#
# for i in range(nn):
#     aa[i] = int(input("Заведите число --> "))
# print(aa)
#
# # i = 0
# # for i in range(1,len(aa)):
# #      if aa[i] > aa[i-1]:
# #         print(aa[i], end=' ')
#
# for i in aa[1:]:
#     if i > i - 1:
#         print(i, end=' ')

# Задача 3. Список. Элементы 1 раз. Порядок встречи.
# Не понимаю как сделать двойной перебор и как не печатать лишних элементов.

aaa = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
bbb = aaa

print(aaa[5:10:1])
print(bbb)

i = 0
dlinna = len(aaa)
print(dlinna)

for i in range(0, len(aaa)):
    while
        if aaa[0] != aaa[0+i]:
            print('', end=' ')
        else:
            print(aaa[0], end=' ')

        i += 1
