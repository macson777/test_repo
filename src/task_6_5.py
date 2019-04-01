# 5) В массиве целых чисел с количеством элементов 19
# определить максимальное число
# и заменить им все четные по значению элементы.


from random import randint


list_1 = []
max_value = 0
for i in range(19):
    list_1.append((randint(0, 100)))
print(list_1)

for j in list_1:
    if j > max_value:
        max_value = j


for n, i in enumerate(list_1):
    if i % 2 == 0:
        list_1[n] = max_value
print(max_value, list_1)