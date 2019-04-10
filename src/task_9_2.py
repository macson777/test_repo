# Создать lambda функцию, которая принимает
# на вход неопределенное количество именных аргументов
# и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

print((lambda names: dict((f'{key}{key}', value) for key, value in names.items()))({'Ilya': 1, 'max': 2, 'Igar': 3}))
