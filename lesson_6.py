# Задание 1.
import time

class TrafficLight:
    mode = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}
    
    def running(self):
        for color, m_time in self.mode.items():
            self.c = color
            print(f'Режим светофора: {self.c}.')
            time.sleep(m_time)
m = TrafficLight()
m.running()

# Задание 2.
class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width
        self.thickness = 5 # толщина асфальта
        self.weight = 25 # кг асфальта с учетом толщины

    def volume(self):
        volume = (self._l * self._w * self.thickness * self.weight) / 1000
        print(f'Для покрытия всей дороги требуется {round(volume)} т асфальта.')

r = Road(5000, 20)
r.volume()

# Задание 3.
class Worker:
   def __init__(self, name, surname, position, wage, bonus):
       self.n = name
       self.s = surname
       self.p = position
       self._i = {'Оклад': wage, 'Премия': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.n} {self.s} {self.p}'

    def get_total_income(self):
        return sum(self._i.values())

p = Position('Илья', 'Петров', 'рабочий', 10000, 5000)

print(p.get_full_name(), p.get_total_income())

# Задание 4.
class Car:
    def __init__(self,name, speed, color, is_polise = False):
        self.n = name
        self.s = speed
        self.c = color
        self.i = is_polise

    def go(self):
        return f'\nАвтомобиль {self.n}({self.c} цвет) поехал.'
    def stop(self):
        return f'\nАвтомобиль остановился.'
    def turn(self, direction):
        return f'\nАвтомобиль повернул {direction}.'
    def show_speed(self):
        return f'\nСкорость автомобиля {self.s} км/ч.'

class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            return f'\nВнимание! Cкорость автомобиля превышает 60 км/ч.'
        else:
            return f'\nCкорость автомобиля {self.s} км/ч.'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            return f'\nВнимание! Скорость автомобиля превышает 40 км/ч.'
        else:
            return f'\nCкорость автомобиля {self.s} км/ч.'

class PoliceCar(Car):
    pass

t_c = TownCar('Mazda', 61, 'красный', False)
print(t_c.go(), t_c.show_speed(), t_c.turn('налево'), t_c.stop())

s_c = SportCar('Honda', 70, 'зеленый', False)
print(s_c.go(), s_c.show_speed(), s_c.turn('направо'), s_c.stop())

w_c = WorkCar('MAN', 50, 'красный', False)
print(w_c.go(), w_c.show_speed(), w_c.turn('налево'), s_c.turn('направо'), w_c.stop())

p_c = PoliceCar('Kia', 40, 'синий', True)
print(p_c.go(), p_c.show_speed(), p_c.stop())

# Задание 5.
class Stationery:
    def __init__(self, title):
        self.t = title
    def draw(self):
        print(f'Запуск отрисовки. Используем {self.t}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Используем ручка {self.t}.')

class Pensil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Используем карандаш {self.t}.')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки. Используем маркер {self.t}.')

s = Stationery('канцелярская принадлежность.')
s.draw()

p = Pen('красная')
p.draw()

p = Pensil('графитный')
p.draw()

h = Handle('перманентный')
h.draw()
