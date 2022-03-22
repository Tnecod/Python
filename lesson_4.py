# Задание 1.
from sys import argv
script_name, hour_work, rate_hour, bonus = argv
print("Расчет зарплаты!")
print("Отработано часов:", hour_work)
print("Ставка за час:", rate_hour)
print("Премия:", bonus)
income = ((float(hour_work) * float(rate_hour)) + float(bonus))
print("Заработная плата:", round(income, 2))

# Задание 2.
print('Задание 2.')
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst_new = []

lst_new = [el for i, el in enumerate(lst) if i > 0 and lst[i] > lst[i - 1]]
print(lst)
print(f'Новый список: {lst_new}')

# Задание 3.
print('Задание 3.')
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# Задание 4.
print('Задание 4.')
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(lst)

lst_new = [el for el in lst if lst.count(el) == 1]
print(f'Новый список: {lst_new}')

# Задание 5.
print('Задание 5.')
from functools import reduce

lst = [el for el in range(100,1001) if el % 2 == 0]
lst_new = reduce(lambda a,b: a * b, lst)
print(lst_new)

# Задание 6.
print('Задание 6.')
from itertools import count, cycle
var_1 = int(input('Число начала итерации: '))
var_2 = int(input('Число завершения цикла: '))
var_3 = int(input('Количество повторения элементов списка: '))
lst = []

for el in count(var_1):
    if el > var_2:
        break
    else:
        lst.append(el)
print(lst)

# вторая часть задания 6
lst_new = []
for i, el in enumerate(cycle(lst), 2):
    lst_new.append(el)
    if i > var_3 * len(lst):
         break
print(lst_new)

# Задание 7.
print('Задание 7.')
def fact(n):
    el = 1
    for i in range(1, n + 1):
        el = el * i
        yield el
n = int(input("Факториал какого числа считать? "))
for el in fact(n):
    print(el)