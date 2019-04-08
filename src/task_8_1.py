# Написать функцию принимающая на вход неопределенным количеством аргументов
# и именованный аргумент mean_type.
# В зависимости от mean_type вернуть
# среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.


def geometr(args):
    geom = 1
    for i in args:
        geom *= i ** (1 / len(args))
    return geom


def average(args):
    summ = 0
    for i in args:
        summ += i
    aver = summ / (len(args))
    return aver


def numbers_operation(*args, **kwargs):
    for key, value in kwargs.items():
        k = value
    if k == 'average':
        print(average(args))
    elif k == 'geometr':
        print(geometr(args))






numbers_operation(5, 8, 55, 67, 8, 2, 3, mean_type='geometr')
