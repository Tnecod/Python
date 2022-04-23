# Задание 1.
class Data():
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date):
        day, month, year = map(int, date.split('.'))
        date_1 = cls(day, month, year)
        return date_1

    def string_to_db(self):
        return print(f'{self.day}-{self.month}-{self.year}')

    @staticmethod
    def valid(date):
        day, month, year = map(int, date.split('.'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year:
            return print(f'Данные введены верно:')
        else:
            print('Неправильно ввели дату:')

var = '-10.04.2022'
date1 = Data.valid(var)
date1 = Data.from_string(var)
date1.string_to_db()

var = '10.04.2022'
date1 = Data.valid(var)
date1 = Data.from_string(var)
date1.string_to_db()

# Задание 2.
class Check_null(Exception):
    def __init__(self, res):
        self.res = res

def div():
    try:
        var_1 = float(input('Введите делимое: '))
        var_2 = float(input('Введите делитель: '))
        if var_2 == 0:
            raise Check_null("Деление на ноль!")
        else:
            res = round(var_1 / var_2, 2)
            return res
    except ValueError:
        return "Это не число!"
    except Check_null as error:
        return error

print(div())

# Задание 3.
class Check_lst:
    def __init__(self, *args):
        self.my_list = []

    def My_input(self):
        while True:
            try:
                el = int(input('Введите значение и нажмите "enter": '))
                next = input('Продолжаем y/n?: ')
                self.my_list.append(el)
                if next == 'n':
                    print (f'Результат: {self.my_list}')
                    break
                print(f'Текущий список: {self.my_list}')
            except:
                next = input(f'"Это не число! Продолжаем y/n?: ')
                if next == 'n':
                    print(f'Результат: {self.my_list}')
                    break

res = Check_lst()
print(res.My_input())

# Задание 4-6.
class Warehouse:
    def __init__(self):
        self._dict = {}

    # прием на склад
    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)
    # выдача со склада
    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, quantity, year):
        self.name = name
        self.quantity = quantity
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.quantity} {self.year}'


class Printer(Equipment):
    def __init__(self, name, quantity, year, type_print):
        super().__init__(name, quantity, year)
        self.type_print = type_print

    def __str__(self):
         return f'{self.name} {self.quantity} {self.year} {self.type_print}'

class Scaner(Equipment):
    def __init__(self, name, quantity, year, dpi):
        super().__init__(name, quantity, year)
        self.dpi = dpi
    def __str__(self):
         return f'{self.name} {self.quantity} {self.year} {self.dpi}'

class Xerox(Equipment):
    def __init__(self, name, quantity, year, format):
        super().__init__(name, quantity, year)
        self.format = format
    def __str__(self):
         return f'{self.name} {self.quantity} {self.year} {self.format}'

warehouse = Warehouse()
scaner = Scaner('hp100', 3, 2022, '300*600')
warehouse.add_to(scaner)
scaner = Scaner('canon101', 1, 2020, '300*600')
warehouse.add_to(scaner)
printer = Printer('Canon100', 3, 2018, 'jet')
warehouse.add_to(printer)
xerox = Xerox('xerox100', 1, 2021, 'A4')
warehouse.add_to(xerox)
# выводим склад
print('Остатки на складе:')
print(warehouse._dict)
# забираем со склада и выводим остатки
warehouse.extract('Scaner')
print('Остатки на складе после выдачи:')
print(warehouse._dict)

# Задание 7.
class Complex_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма чисел:')
        return f'({self.a + other.a}+{self.b + other.b}j)'

    def __mul__(self, other):
        print(f'Произведение чисел:')
        return f'({(self.a * other.a) - (self.b * other.b)}+{self.b * other.a + self.a * other.b}j)'

z_1 = Complex_num(1.1, 1)
z_2 = Complex_num(1.1, 4)

print(z_1 + z_2)
print(z_1 * z_2, f'\n')

print(f'Проверка:')
print(f'1.1+1j + 1.1+4j = {complex(1.1, 1)+complex(1.1, 4)}')
print(f'1.1+1j * 1.1+4j = {complex(1.1, 1)*complex(1.1, 4)}')
