# Задание 1. Найди все буквы в первой строке, которые отсутствуют во второй.

a = set("Python")
b = set("Programming language")
for i in a:
    if i not in b:
        print(i, end="\t")
print()

v2 = [i for i in a if i not in b]
print(v2)
print()

# Задание 2. Посчитайте гласные буквы в строке.

gl = "уеыаоэяию"
aa = "Привет, мир"
gl_in_aa = []
for i in aa:
    if i in gl:
        print(i, end="\t")
print()
# Второй способ
vv2 = [i for i in aa if i in gl]
print(vv2)
print()
# Задание 3. Найти все буквы присутствующие хотя бы в одно строке.
aaa = "test"
bbb = "string"
ccc = set(aaa + bbb)
print(ccc)
print()
# Задание 4. Ввод уникальных букв из двух строк.
# Легкий способ
uniq_list = set(list("hello")).symmetric_difference(set(list("world")))
print(uniq_list)

# Способ через цикл.
aaaa = list("hello")
bbbb = list("world")
cccc = []

for i in aaaa:
    if i not in bbbb:
        cccc.append(i)

for i in bbbb:
    if i not in aaaa:
        cccc.append(i)

print(cccc)