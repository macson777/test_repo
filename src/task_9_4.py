# Создать универсальны декоратор, который меняет
# порядок аргументов в функции на противоположный.


def my_decorator(func):
    def do_some_staff(*arg):
        list_a = arg[::-1]
        return func(list_a)
    return do_some_staff


@my_decorator
def my_func(*args):
    print(*args)


my_func(2, 7, 8, 16, 22, ['ff'], 18, 8, 9, 11, 10, 13, 14, 15)
