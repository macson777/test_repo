# Дан массив целых чисел A.
# Найти суммы положительных
# и отрицательных элементов массива,
# используя функцию определения суммы.


from random import randint

def summa(args):
    sum_otr = []
    sum_pol = []
    for number in args:
        if number < 0:
            sum_otr.append(number)
        elif number > 0:
            sum_pol.append(number)
    return sum(sum_otr), sum(sum_pol)


n = int(input('input number of elemnts in list\n'))
list_1 = []
for i in range(n):
    list_1.append(randint(-50, 50))
print(list_1)
print(summa(list_1))



