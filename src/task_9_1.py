# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.

list_a = ['Slovo', 'Zadanie', 'Privet', 'Kolobok']
list_b = [f'{i} - {list_a[i]}' for i in range(len(list_a))]
print(list_b)

