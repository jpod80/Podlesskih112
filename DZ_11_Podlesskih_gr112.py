# # Задание 1.
#
dic_a = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
dic_b = dict()
dic_b["name"] = dic_a.pop("name")
dic_b["salary"] = dic_a.pop("salary")
print(dic_a)
print(dic_b)
print()

# # Задание 2. Переименовать ключ.
dic_c = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# dic_c['location'] = dic_c.pop('city')  
dic_ccc = {"location": "New York"}
dic_c.pop("city")
dic_c.update(dic_ccc)
print(dic_c)




