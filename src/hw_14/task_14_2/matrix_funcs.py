def max_elem_matrix(matrix):
    elem_max = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > elem_max:
                elem_max = elem
    return elem_max


def min_elem_matrix(matrix):
    elem_min = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < elem_min:
                elem_min = elem
    return elem_min


def summa_elem_matrix(matrix):
    summa = 0
    for row in matrix:
        for elem in row:
            summa += elem
    return summa

