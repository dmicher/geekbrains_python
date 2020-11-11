from lesson6.Car import Car

class TownCar(Car):
    """Класс "Городской автомобиль" для задания 4"""
    def __init__(self, color: str):
        return super().__init__(base_speed=20, max_accelerations=6, name="городской автомобиль", color=color)
    
    def speed_up(self):
        super().speed_up()
        if self._speed_ > 60:
            print("Впереди камера на 60!")

class SportCar(Car):
    """Класс "Спортивный автомобиль" для задания 4"""
    def __init__(self, color: str):
        return super().__init__(base_speed=35, max_accelerations=6, name="спортивный автомобиль", color=color)

class WorkCar(Car):
    """Класс "Рабочий автомобиль" для задания 4"""
    def __init__(self):
        return super().__init__(base_speed=15, max_accelerations=6, name="рабочий автомобиль", color=color)

    def speed_up(self, color: str):
        super().speed_up()
        if self._speed_ > 40:
            print("Внимание! Вы превышаете скоростной лимин. Сбросьте скорость", color=color)

class PoliceCar(Car):
    """Класс "Полицейский" для задания 4"""
    def __init__(self, color: str):
        return super().__init__(base_speed=25, max_accelerations=6, name="полицейский автомобиль", 
                                color=color, is_police=True)

