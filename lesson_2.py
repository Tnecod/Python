# Задание 1
print('Задание 1.')

lst = ['Max', 234, 2.78, [1, 3, 5], {'one': 1, 'two': 2}]
print(f'Cписок: {lst}')
num = 1

for i in range(len(lst)):
    print(f'{num} элемент в списке: {lst[i]}, тип: {type(lst[i])}')
    num += 1
print('Конец списка')

# Задание 2
print('Задание 2.')

lst = input("Введите элементы списка через пробел: ").split()
print(f'Ввведенный список: {lst}')

lst[:-1:2], lst[1::2] = lst[1::2], lst[:-1:2]
print(f'Измененный список: {lst}')

# Задание 3
print('Задание 3. Вариант 1.')

i = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season = ['зима', 'весна', 'лето', 'осень']

if i == 12 or i <= 2:
    print(f'Время года - {season[0]}.')
elif 3 <= i <= 5:
    print(f'Время года - {season[1]}.')
elif 6 <= i <= 8:
    print(f'Время года - {season[2]}.')
else:
    print(f'Время года - {season[3]}.')

print('Задание 3. Вариант 2.')

season = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
num = int(input('Введите номер месяца от 1 до 12: '))

for i in season:
    if num in season[i]:
        print(f'Время года - {i}.')

# Задание 4
print('Задание 4.')

lst = input('Введите строку из нескольких слов, разделённых пробелами: ').split()

for i, num in enumerate(lst, 1):
    print(f'{i}. {num[:10]}')

# Задание 5
print('Задание 5.')

num = int(input('Введите целое число: '))
lst = [8, 6, 3, 3, 1]
print(f'Начальный список: {lst}')

for i in range(len(lst)):
    if num > lst[i]:
        lst.insert(0, num)
        break
    elif num < lst[-1]:
        lst.append(num)
        break
    elif num == lst[i] or lst[i] > num > lst[i + 1]:
        lst.insert(i + 1, num)
        break
print(f'Изменненый список: {lst}')

# Задание 6.
print('Задание 6.')

print('Структура "Товары": Группа товаров - товар - цена - ко-во - един. измерения')
print('Введите цифру 0 если все товары введены ')
product = '0'
price = 0
quantity = 0
unit_m = '0'
lst = []
dic = {'название': [], 'цена': [], 'ко-во': [], 'ед.': []}

for i in range(1, 100):
    print(f'Tовар {i}.')
    product = input('Название товара: ')
    if product != '0': # если 0, то завершаем цикл
        price = float(input('Цена товара: '))
        quantity = float(input('Количество: '))
        unit_m = input('Единица измерения: ')
        lst_1 = (i, {'название': product, 'цена': price, 'ко-во': quantity, 'ед.': unit_m})
        lst.extend(lst_1) # переводим кортеж в список
        dic['название'].append(product) # добавляем значение по ключу
        dic['цена'].append(price)
        dic['ко-во'].append(quantity)
        dic['ед.'].append(unit_m)
    else:
        break
print(*lst, sep='\n')
print('\nСводные данные: ')
for keys,values in dic.items(): # выводим ключи со значениями построчно
    print(keys, values)
