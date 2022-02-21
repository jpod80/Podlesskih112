# Задание 1. Функцтия slicer() на вход принимает кортеж и случайный элемент.
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.

import random as r

def slicer(list1):
    r1 = r.randint(1, 10)
    a2 = []             # массив для наглядности
    a2.append(list1)
    a2.append(r1)
    t2 = tuple(a2)

    a3 = []
    cont = 0
    for i in list1:
        if i == r1 and cont == 0:
            a3.append(i)
            cont = 1
        elif cont == 1:
            a3.append(i)
    print("Изначальные данные: ", t2)
    print("Итоговый массив от цикла:", tuple(a3))

    # Решение через методы
    if r1 in list1:
        s = list1.index(r1)
        print("Через методы:", list1[s:len(list1)])
    else:
        print("Значение через методы не найдено")


# Входные данные
k0 = (1, 2, 3)
k1 = (1, 8, 3, 4, 8, 8, 9, 2)
k2 = (1, 2, 8, 5, 1, 2, 9)
rand_k_i = 1

# Запуск функции
slicer(k1)
print(end="\n\n")


# Задание 2. Заполнить 1 кортеж десятью случайными числами.
import random as r
def random_tuples():
    m_1 = []
    m_2 = []
    i = 0
    while i < 10:
        m_1.append(r.randint(0, 5))
        m_2.append(r.randint(-5, 0))
        i += 1
    m_3 = tuple(m_1 + m_2)
    print(m_3)
    print("0 =", m_3.count(0))

random_tuples()
