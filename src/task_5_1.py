matrix_1 = [
    [1, 2, 8, -2, -10],
    [22, 3, 17, 4, 1],
    [7, 8, 8, -2, 9],
    [1, 2, 17, -2, 15],
    [8, 1, 23, 5, 7],
]
i = 0
j = 0
matrix_2 = []
max_value = 0
size = 5
for i in range(size):
    for j in range(size):
        if abs(matrix_1[i][j]) > max_value:
            max_value = abs(matrix_1[i][j])
for i in range(size):
    row = []
    for j in range(size):
       elem_1 = matrix_1[i][j] / max_value
       row.append(str(elem_1))
    matrix_2.append(row)
for i in range(size):
    print(' '.join(matrix_2[i]))











