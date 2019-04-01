# 1) Написать программу, в которой вводятся два операнда Х и Y
# и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака.
# Предусмотреть реакции на возможный неверный знак операции,
# а также на ввод Y=0 при делении.
# Организовать возможность многократных вычислений
# без перезагрузки программа
# (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').



while True:
    x = input('Input x\n')
    y = input('Input y\n')
    sign = input('Input operation "+, -, *, /"\n')
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if sign == '+':
            z = x + y
            print('z =', z)
        elif sign == '-':
            z = x - y
            print('z =', z)
        elif sign == '*':
            z = x * y
            print('z =', z)
        elif sign == '/' and y == 0:
            print('Division by zero')
        elif sign == '/':
            z = x / y
            print('z =', z)
        else:
            print('Wrong value for opertion\n ')
    else:
        print('For x and y input only numbers')

    if sign == '0':
        break







