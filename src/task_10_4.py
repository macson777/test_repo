# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга.[03-15.31]


def checking_lines():
    my_file_1 = open('task_10_4_1.txt')
    lines_1 = my_file_1.readlines()
    my_file_2 = open('task_10_4_2.txt')
    lines_2 = my_file_2.readlines()
    for i, line in enumerate(lines_1):
        if line != lines_2[i]:
            return i
    return -1

    my_file_1.close()
    my_file_2.close()


def main():

    result = checking_lines()
    if result == -1:
        print('files are the same')
    else:
        print('other line', result + 1)

if __name__ == '__main__':
        main()