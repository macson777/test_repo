# Дан список чисел.
# Посчитать сколько раз встречается каждое число.


def search(*args):
    dict_1 = {}
    for i in args:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1

    print(dict_1)
    for key, value in dict_1.items():
        print(f'{key} is found {value} times')


search(1, 5, 99, -8, 67, 1, 4, 5, 99, 34, 45)




