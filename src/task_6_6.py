# 6) Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).



from random import randint

list_1 = []
list_posled = []
posled = []


for i in range(19):
    list_1.append((randint(0, 100)))
print(list_1)

len_list = len(list_1)
i = 1

while i <= len_list:
    if list_1[i] > list_1[i-1]:
        posled.append(list_1[i-1])

        j = i
        while list_1[j-1] < list_1[j]:
            posled.append(list_1[j])
            j += 1
            if j == len_list:
                break
        i = j
        list_posled.append(posled)
    else:
        i += 1
    if i == len_list:
        break

    posled = []
print(list_posled)
print(len(list_posled))