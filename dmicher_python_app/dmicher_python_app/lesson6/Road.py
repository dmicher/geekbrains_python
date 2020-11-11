class Road(object):
    """Класс "Дорога" для задания № 2"""
    __length__: float
    __width__: float

    def __init__(self, length_in_meters: float, width_in_meters: float):
        """Инициирует объект.
        :params length: длина дороги в метрах -> float
        :params width: лишина дороги в метрах -> float"""
        self.__length__ = length_in_meters
        self.__width__ = width_in_meters

    def calculate(self, asphalt_density: float = 25, roadbed_height_in_sm: float = 5) -> float:
        """Расчитывает массу требуемого асфальта
        :params asphalt_density: плотность асфальта в [кг/м*м*см]
        :params roadbed_height_in_sm: толщина дорожного покрытия в [см]
        :returns: масса асфальта в [т], требуемая для покрытия дороги с запасом 10%
        :rtype: float"""
        return self.__length__ * self.__width__ * asphalt_density * roadbed_height_in_sm

    def __str__(self):
        """Переписывает метод строкового отображения"""
        return f"длина {self.__length__} [м], ширина {self.__width__} [м]"