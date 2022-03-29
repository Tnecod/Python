# Задание 1.
import codecs

with codecs.open('text.txt', 'w', 'utf_8_sig') as my_f:
    print('"Enter" для перехода на новую строку, повторно "Enter" - выход')
    while True:
        line = input('Введите данные для строки: ')
        if not line:
            break
        my_f.writelines(line + '\n')

# Задание 2.
import codecs

with codecs.open('text.txt', 'r', 'utf_8_sig') as my_f:
    str = my_f.readlines()
    for el, line in enumerate(str):
        words = line.split()
        print(f'В строке {el + 1}: слов {len(words)}')
    print(f'\nВ файле: строк {el + 1}')

# Задание 3.
import codecs

with codecs.open('text.txt', 'r', 'utf_8_sig') as my_f:
    data = {}
    for line in my_f:
        surname, cash = line.split() 
        data[surname] = float(cash) # присваиваем ключу значение
        if float(cash) < 20000:
            print(f'{surname} : {cash}')
    aver_cash = round(sum(data.values()) / len(data), 2) # для среднего суммируем значения ключей и делим на длину словаря
    print(f'Средняя величина дохода всех сотрудников: \n{aver_cash}')

# Задание 4.
import codecs

rus = ['Один', 'Два', 'Три', 'Четыре']
eng = ['One', 'Two', 'Three', 'Four']

with codecs.open('text.txt', 'r', 'utf_8_sig') as my_f:
    lst = []
    i = 0
    for el in my_f.readlines(): 
        lst.append(el.replace(eng[i], rus[i])) # меняем значения и записываем в список
        i += 1
    with codecs.open('text_new.txt', 'w', 'utf_8_sig') as my_f:
        my_f.writelines(lst)

# Задание 5.
import codecs
res = []

with codecs.open('text.txt', 'w', 'utf_8_sig') as my_f:
    lst = input('Введите числа через пробел: ').split() # сформировали список
    for el in lst:
        my_f.write(el + ' ') # записываем в файл каждый элемент и добавляем пробел
with codecs.open('text.txt', 'r', 'utf_8_sig') as my_f:
    for line in my_f: # считываем строки из файла построчно
        for el in line.split():
            res.append(float(el))
    print(f'Сумма всех чисел: {sum(res)}') # выводим сумму всех чисел файла

# Задание 6.
import codecs, re

dict = {} # словарь с данными из файла
dict_res = {} # итоговый словарь

with codecs.open('text.txt', 'r', 'utf_8_sig') as my_f:
    file = my_f.read()
    my_f.seek(0)
    print(f'Данные из файла: \n{file}\n')
    for line in my_f.readlines():
        sub, info = line.split(':')
        dict[sub] = info.split() # ключу присваиваем значения переменных
        hours = re.findall(r'\d+', info)  # с помощью функции findall() модуля re возвращаем числа из списка
        dict_res[sub] = sum([float(el) for el in hours]) # суммируем числа по каждому ключу

print(f'Словарь: \n{dict_res}')

# Задание 7.
import codecs, json

dict_firm = {} # словарь с фирмами
dict_average = {} # словарь со средней прибылью
lst = [] # итоговый список
# name - название фирмы
# form - форма собственности
# revenue - выручка
# expenses - издержки
# income  - прибыль

with codecs.open('text.txt', 'r', 'utf_8_sig') as my_f:
    file = my_f.read()
    my_f.seek(0)
    print(f'Данные из файла: \n{file}\n')

    for line in my_f.readlines():
        name, form, revenue, expenses = line.split() # разбиваем строку файла на переменные
        income = float(revenue) - float(expenses)
        dict_firm[name] = income
    lst.append(dict_firm) # словарь добавляем в список
    i = 0
    var = 0
    for key, value in dict_firm.items(): # определяем среднюю прибыль
        if value > 0:
            var = var + value
            i = i + 1 # число для деления, чтобы получить среднее значение
        dict_average['average_profit'] = round(var / i, 2)
    if var == 0: # если средняя прибыль равна нулю(все компании с убытком)
        print('Все компании с убытком!')
    lst.append(dict_average) # добавляем среднюю прибыль в список

print(f'Список: \n{lst}')

with codecs.open('my_f.json', 'w', 'utf_8_sig') as my_f:
    json.dump(lst, my_f) # список сохранили в json-файл
    print(f'\njson-файл: \n{json.dumps(lst)}') # печать содержимого json-файла
