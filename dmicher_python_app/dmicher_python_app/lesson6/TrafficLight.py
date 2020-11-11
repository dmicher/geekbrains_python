from lesson6.TrafficLightColor import TrafficLightColor
from tools import DmicherException
from itertools import cycle

class TrafficLight():
    """Светофор для задания № 1"""
    __colors__= {"красный": 7.0, "жёлтый": 2.0, "зелёный": 14.0}
    __color__ = None
    __colors_generator__ = None

    def __init__(self):
        """При запуске светофора сразу назначает первый цвет"""
        self.__colors_generator__ = self.__next_color__()
        self.__color__ = next(self.__colors_generator__) # TrafficLightColor("красный", 7.0, 0)
        pass

    def set_color_time(self, color: str, new_time: float) -> None:
        """Управляет настройками светофора: изменяет время для указанного цвета
        :params color: настраиваемый цвет: "красный", "жёлтый" или "зелёный" -> str
        :params new_time: устанавливаемое время действия цвета -> float
        """
        color = color.strip().lower()
        if color in self.__colors__:
            self.__colors__[color] = new_time
        else:
            raise DmicherException("На светофоре отсутствует указанный цвет")

    def running(self) -> (str, float):
        """Возвращает текущее состояние светофора: цвет и время до следующего цвета
        (статус светофора не зависит от частоты обращения к этому методу - только от времени)
        :returns: цвет светофора и оставшееся время до переключения
        :rtype: (str, float)"""
        # Если цвет должен был смениться с последнего обращения к статусу светофора, переключает 
        # светофор, пока не израсходует натикавшее время. Затем выводит сстатус светофора
        while self.__color__.time_left() <= 0: 
            self.__color__ = next(self.__colors_generator__)
        return self.__color__.name(), self.__color__.time_left()
            
    def __next_color__(self, time_passed: float = .0) -> TrafficLightColor:
        """По бесконечному циклу выдаёт следующий цвет из настроенного списка"""
        for key in cycle(TrafficLight.__colors__.keys()):
            yield TrafficLightColor(key, self.__colors__[key], time_passed)

