# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)[03-10.32]

str_1 = ['dovod', 'radar', 'terem']

def palindrom(str):
    for word in str:
        if word == word[::-1]:
            print(f'{word} palindrom')


palindrom(str_1)


