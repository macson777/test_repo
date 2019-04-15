# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы
# и сохранить в другой файл. [my-files-t01]


import json
from random import randint


def create_matrix(random_from=1, random_to=10):
    random_matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append((randint(random_from, random_to)))
        random_matrix.append(row)
    return random_matrix


def print_matrix(filename, matrix):
    with open(filename, "w") as new_file:
        for line in matrix:
            json_line = json.dumps(line)
            new_file.write(f'{json_line}\n')


def read_matrix(filename):
    matrix = []
    with open(filename) as read_file:
        for line in read_file.readlines():
            matrix.append(json.loads(line))
    return matrix


def main():

    print_matrix('task_10_5_1.txt', create_matrix())
    matrix = read_matrix('task_10_5_1.txt')
    for i, line in enumerate(matrix):
        for j, elem in enumerate(line):
            if elem % 2 == 0:
                matrix[i][j] = 0

    print_matrix('task_10_5_2.txt', matrix)


if __name__ == '__main__':
        main()
