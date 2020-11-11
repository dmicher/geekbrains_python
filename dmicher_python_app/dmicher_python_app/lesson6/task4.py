# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую 
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение 
# о превышении скорости.

import lesson6.SubCars as auto

def run():
    """Выполняет задание 4 для урока 6"""
    print("\r\nЗадание 4\r\n")

    print("Этот скрипт представляет собой технологическую \"песочницу\".")
    print("Вы выбираете машину и управляете ею с помощью команд из консоли.")
    print("(из этого могла бы получиться игра, будь на это больше времени и желания)\r\n")
    print("Для пробы доступны следующие типы автомобилей:")
    cars = {"г": "городской автомобиль", "с": "спортивный автомобиль", 
            "р": "рабочий автомобиль", "п": "полицейский автомобиль"}
    for key in cars.keys():
        print(f"\t{key} - " + cars[key])

    user_input = input("Выберите свой автомобиль (кириллица): ")
    if user_input not in ('г','с','р','п'):
        print("Нет такого автомобиля. Работа скрипта завершена.")
        return
    car_type = user_input

    user_input = input("Введите цвета автомобиля (ед. число, муж.род, например \"синий\"): ")
    color = user_input.strip().lower().capitalize() if not user_input == '' and not user_input.isspace() else "Чёрный"

    car = None
    if car_type == 'г':
        car = auto.TownCar(color)
    elif car_type == 'с':
        car = auto.SportCar(color)
    elif car_type == 'р':
        car = auto.WorkCar(color)
    elif car_type == 'п':
        car = auto.PoliceCar(color)
    
    print("Вы садитесь в " + str(car).lower() + ". Приятной езды! (подсказка - ввести ?)")

    while True:
        user_input = input("> ")
        if user_input == "?":
            print("Доступные команды:")
            for name, value in (('?', "эта подсказка"),
                                ('ц', "ускориться"),
                                ('ы', "замедлиться"),
                                ('ф', "поворот налево"),
                                ('в', "поворот направо"),
                                ('с', "разворот"),
                                (' ', "продолжать движение"),
                                ('!', "резко остановиться"),
                                ('й', "закончить езду")):
                print("\t" + name + " - " + value)
        if user_input == 'й':
            print("Езда завершена.")
            break
        elif user_input == '!':
            car.stop()
        elif user_input in (' ', ''):
            car.wait()
        elif user_input == 'с':
            car.direction('o')
        elif user_input == 'в':
            car.direction('r')
        elif user_input == 'ф':
            car.direction('l')
        elif user_input == 'ц':
            car.speed_up()
        elif user_input == 'ы':
            car.slow_down()
        else:
            print("Неизвестная команда. Повторите ввод (h - подсказка)")

    print("Задание выполнено\r\n")
