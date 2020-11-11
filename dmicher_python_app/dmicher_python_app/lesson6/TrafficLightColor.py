import time

class TrafficLightColor:
    """Цвет сфетофора"""
    __color_name__: str
    __exposition_time__: float
    __time_start__: float

    def __init__(self, color_name: str, exposition_time: float, time_passed: float):
        """Инициирует объект:
        :params color_name: название имени цвета
        :params exposition_time: сколько времени цвет должен отображаться
        :params time_passed: сколько времени прошло с момента, когда цвет должен был быть включен"""
        self.__color_name__ = color_name
        self.__exposition_time__ = exposition_time - abs(time_passed)
        self.__time_start__ = time.time()

    def time_left(self):
        """Сколько времени (в секундах) осталось до завершения цвета"""
        return self.__exposition_time__ - (time.time() - self.__time_start__)

    def name(self) -> str:
        """Название цвета"""
        return self.__color_name__