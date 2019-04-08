def square(*args):
    a = args[0]
    b = args[1]
    c = args[2]
    d = (b ** 2) - 4 * a * c
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    print(x_1)
    print(x_2)


square(3, -14, -5)

