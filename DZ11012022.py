# Group 112
# Задание 1. Линия из символов.
a = int(input("Количество символов -->"))
b = input("Тип символа -->")
c = int(input("Ориентация символа. Укажите:\n 0 - горизонтальная \n 1 - Вертикальная \n -->"))

if c == 1:
    i = 0
    while i < a:
        print(b, end='\n')
        i += 1
elif c == 0:
    i = 0
    while i < a:
        print(b, end='\t')
        i += 1


# Задание 2. Среднее арифметическое последовательности дробных чисел.
aa = int(input("Количество чисел участвующих в расчете -->"))

i = 0
sum_numbers = 0
min_numberAA = 100000000000000000000000
max_numberAA = -100000000000000000000000

while i < aa:
    numberAA = float(input('Заведите число  -->'))
    i += 1
    sum_numbers = sum_numbers + numberAA
    min_numberAA = numberAA if numberAA < min_numberAA else min_numberAA
    max_numberAA = numberAA if numberAA > max_numberAA else max_numberAA

print('Количество чисел ', aa)
print('Среднее арифметическое ', sum_numbers/aa)
print('Минимальное число ', min_numberAA)
print('Максимальное число ', max_numberAA)


# Задание 3. Про палиндром.
aaa = input("Заведите число или слово -->")
bbb = list(aaa)
ccc = len(aaa)
i = 1
# print(bbb[i-1])
# print(bbb[-i])
while i <= (ccc/2):
    if bbb[i-1] == bbb[-i]:
        print("OK")
    else:
        print("фигня")
        break
    i += 1
print("палиндром")
# print(aaa,ccc, bbb)
# print(aaa[-1:])
# print(aaa[:1])