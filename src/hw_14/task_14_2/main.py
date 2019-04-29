from matrix_classes import Matrix
from matrix_funcs import max_elem_matrix, min_elem_matrix, summa_elem_matrix


data = [
    [1, 2, 8, -2, -10],
    [22, 3, 17, 4, 1],
    [7, 8, 8, -2, 9],
    [1, 2, 17, -2, 15],
    [8, 1, 23, 5, 7],
]
matrix = Matrix(data)
print(matrix)
print(max_elem_matrix(matrix))
print(min_elem_matrix(matrix))
print(summa_elem_matrix(matrix))

