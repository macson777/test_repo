def change_0_1():
    my_file_1 = open('task_10_2_1.txt')
    with open('task_10_2_2.txt', 'w') as my_file_2:
        for line in my_file_1:
            for letter in line:
                if letter == '0':
                    letter = '1'
                elif letter == '1':
                    letter = '0'
                my_file_2.write(letter)

    my_file_1.close()
    my_file_2.close()


def main():

    change_0_1()

if __name__ == '__main__':
        main()
