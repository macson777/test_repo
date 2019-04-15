def line_func():
    my_file_1 = open('task_10_3_1.txt')
    my_file_2 = open('task_10_3_2.txt', 'w')
    my_file_3 = open('task_10_3_3.txt', 'w')
    count_1 = 0
    while True:
        count_1 += 1
        line = my_file_1.readline().strip()
        if not line:
            break
        if count_1 % 2 == 0:
            my_file_2.write(f'{line}\n')
        elif count_1 % 2 != 0:
            my_file_3.write(f'{line}\n')
    my_file_1.close()
    my_file_2.close()
    my_file_3.close()


def main():

    line_func()

if __name__ == '__main__':
        main()
