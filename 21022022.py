# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# c = []
#
# for i in range(1,11):
#     # d = i * i
#     c.append(i * i)
# print(c)

# lst = []
# n = int(input("Колич элементов"))
# for num in range(n):
#     x = int(input("Кратное 3 число"))
#     list.append(x)
# print(lst)

a = [1, 2, 3]
b = [11, 22, 33]
c = []
for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])
print(c)



d = []
n=int(input('Введите количество циклов: '))
for i in range(n):
    x=int(input('Введите число: '))
    d.append(x)
print(d)
k=int(input('Введите index: '))
d.pop(k)
print(d)
