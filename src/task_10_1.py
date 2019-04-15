# В конец существующего текстового файла
# записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.[03-15.6]


def add_strings():
    with open('task_10_1.txt', 'a') as my_file:
        for i in range(3):
            input_1 = input('input string\n')
            string = f'\n{input_1}'
            my_file.write(string)


def main():

    add_strings()

if __name__ == '__main__':
        main()
