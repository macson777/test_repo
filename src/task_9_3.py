# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.


def my_decorator(func):
    def do_some_staff(*arg):
        list_a = []
        for number in arg:
            if number % 2 != 0:
                list_a.append(number)
        return func(list_a)
    return do_some_staff


@my_decorator
def my_func(*args):
    print(*args)


my_func(2, 7, 8, 16, 22, 14, 18, 8, 9, 11, 10, 13, 14, 15)