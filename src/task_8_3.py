# Рассчитать значение х определив
# и использовав необходимую функции. [02-5.1-BL01]


def formula(*args):
    for i in args:
        x = (i ** 0.5 + i) / 2
    return x


print(formula(5, 12, 9))


