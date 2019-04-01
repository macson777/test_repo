# 7) Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.



from random import randint
n = input('Input n\n')
n = int(n)
i = 0
j = 0
matrix_1 = []

for i in range(n):
    row_max = 0
    row = []
    for j in range(n):
        row.append((randint(0, 50)))
    matrix_1.append(row)

    print(matrix_1[i])


    for l, r in enumerate(matrix_1[i]):
        if r > row_max:
            row_max = r
            k = l

    a = matrix_1[i][i]
    matrix_1[i][i] = row_max
    matrix_1[i][k] = a


print('Updated matrix\n')
for i in range(n):
    print(matrix_1[i])
