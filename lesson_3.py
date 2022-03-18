# Задание 1.
print('Задание 1.')
def func(a, b):
    while b == 0: # проверка на ноль
        print('Ошибка, деление на ноль!')
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
    res = a / b
    print('Результат:', round((res),2))

func(float(input('Введите первое число: ')), float(input('Введите второе число: ')))

# Задание 2.
print('Задание 2.')
def func(name, surnameage, birth, email, tel):
    print(f'Имя: {name}, фамилия: {surnameage}, дата рождения: {birth},'
          f' email: {email}, телефон: {tel}')

func(name = input('Имя: '), surnameage = input('фамилия: '), birth = input('дата рождения: '),
     email = input('email: '), tel = input('телефон: '))

# Задание 3.
print('Задание 3.')
def func(a, b, c):
    res = (a + b + c) - min(a, b, c) # функция min перебирает и возвращает минимальное значение из списка
    print(f'Сумма двух наибольших чисел: {res}')

func(float(input('Введите первое число: ')),
        float(input('Введите второе число: ')),
        float(input('Введите третье число: ')))

# Задание 4.
print('Задание 4. вариант 1')
def func(a, b):
    res = a ** b
    print(f'Результат: {res}')

func(float(input('Введите действительное положительное число: ')),
     int(input('Введите целое отрицательное число: ')))

print('Задание 4. вариант 2')
def func(a, b):
    b = abs(b)  # модуль числа
    c = a
    for i in range(b - 1):
        c = c * a
    c = 1 / c
    print(f'Результат: {c}')

func(float(input('Введите действительное положительное число: ')),
     int(input('Введите целое отрицательное число: ')))

# Задание 5
print('Задание 5.')
def func():
    res = 0
    while True:
        var = input('Введите через пробел числа или stop для завершения: ').split()
        for i in var:
            try:
                if i == 'stop':
                    print(f'Сумма введенных чисел: {res}')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Повторите ввод чисел или stop для завершения!')
        print(f'Сумма введенных чисел: {res}')
func()

# Задание 6
print('Задание 6.')
# Задание 6.
def func(word):
    lst = []
    lst.append(word.title())
    return ''.join(lst)
print(func(input('Введите слово: ')))

# Задание 7
print('Задание 7.')
print(func(input('Введите несколько слов через пробел: ')))