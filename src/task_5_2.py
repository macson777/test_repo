m = int(input('Input numerical value m\n'))
n = int(input('Input numerical value n(n will be > m)\n'))
for number in range(m, n + 1):
    dividers = []
    for divider in range(2, number):
        if number % divider == 0:
            dividers.append(str(divider))
    print(f'{number}: {", ".join(dividers)}')



