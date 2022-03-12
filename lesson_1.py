# задание 1
number = 12
line = 'Max'
number_1 = 12.5
print(number, line, number_1)
age = input('Введите ваш возраст: ')
name = input('Введите ваше имя: ')
print(f'Имя: {name}, возраст: {age} лет.')


# задание 2
number = int(input('Введите время в секундах: '))
hour = number // 3600
minute = (number % 3600) // 60
second = (number % (24 * 3600)) % 60
print(f'Time: {hour:02d}:{minute:02d}:{second:02d}')


# задание 3
n = input('Введите число: ')
n_1 = int(n + n)  # склеиваем числа и переводим в число
n_2 = int(n + n + n)  # склеиваем числа и переводим в число
n = int(n)
result = n + n_1 + n_2
print(result)


#задание 4
number = int(input('Введите целое положительное число: '))
number_max = 0

while number > 0:
    last = number % 10 # выделяем последнюю цифру числа
    if last > number_max:
        number_max = last # сохраняем цифру, если она больше последней цифры в числе
    number = number // 10 # уменьшили число убрав последнюю цифру числа
print('Самая большая цифра в числе: ' , number_max)


#задание 5-6
revenue = float(input('Укажите выручку фирмы: '))
expenses = float(input('Укажите издержки компании: '))
income = float(revenue - expenses) # формула прибыли
profitability = 0

if income > 0:
    print('Поздравляем, фирма работает с прибылью.')
    profitability = income / revenue # формула рентабельности
    staff = int(input('Введите количество сотрудиков в фирме: '))
    income_staff = income / staff # формула прибыли на одного сотрудника
    print('Рентабельность выручки: ', round(profitability, 2))
    print('Прибыль на одного сотрудника составляет: ', round(income_staff, 2), 'руб.')
else:
    print('У фирмы убыток. Необходимо увеличивать выручку при сохранении издержек!')


#задание 7
a = float(input('Введите количество км для достижения результата: '))
b = float(input('Введите расстояние пробежки в 1-ый день: '))
print('Для достижения результата будем увеличивать каждый день расстояние на 10%')

n = 1
while b < a:
    if n > 0:
        print(n, 'день: ', b)
        n += 1
    b =round(float(b + (b*(10/100))), 2)
print(n, 'день: ', b)
print('На', n, 'день спортсмен достиг результата в', b, 'км.')
