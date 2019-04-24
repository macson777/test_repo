# 3) Два натуральных числа называют дружественными,
# если каждое из них равно сумме всех делителей другого,
# кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

m = 205
n = 10000

for number in range(m, n + 1):
    sum_1 = 0
    dividers = []
    for divider in range(1, number // 2 + 1):
        if number % divider == 0:
            sum_1 += divider


    if sum_1 in range(sum_1, n + 1):
        sum_2 = 0
        for divider_1 in range(1, sum_1 // 2 + 1):
            if sum_1 % divider_1 == 0:
                sum_2 += divider_1
        if number == sum_2 and sum_1 > number:
            print(number, sum_1)




