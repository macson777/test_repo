# 2) Дано число.
# Найти сумму и произведение его цифр.

number = input('input number\n')
summa = 0
comp = 1
for i in number:
    summa += int(i)
    comp *= int(i)
print('Summa =', summa, ';', 'Proizvedenie =', comp)

