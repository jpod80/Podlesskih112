# def check_password(username):
#     username = str(username)
#     sum = 0
#     sum1 = 0
#     for i in username:
#         c = int(i)
#         if c % 2 == 0:
#             sum += c
#         else:
#             sum1 += c
#     print('Сумма четных элементов: ', sum)
#     print('Сумма нечетных элементов: ', sum1)
#
# check_password(754622)
#
#
# cp=tuple([2**i for i in range(12)])
# print(cp)

from random import randint
# def fufunc(s):
#     ls = []
#     [ls.append(i)for i in s if i not in ls]
#     print(ls)
#     return tuple(ls)
# s = [1, 2, 3, 3, 2]
# print(fufunc(s))
#


# s = {1,2,3,3,3}
# print(s)


# abcd = int(input())
# d = abcd % 10
# c = abcd // 10 % 10
# b = abcd // 100 % 10
# a = abcd // 1000
#
# print(a, b, c, d)

a = int(input())
aa = str(a)*2
aaa = str(a)*3
su = int(a) + int(aa) + int(aaa)
print(su)
