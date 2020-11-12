from abc import ABC, abstractmethod, abstractproperty

class Сlothes(ABC):
    """Класс "Одежда" для задания 2"""
    @property
    @abstractmethod
    def fabric_count(self):
        """Абстрактный метод для проведения расчётов ткани"""
        pass

    @property
    @abstractmethod
    def name(self):
        """Абстрактное свойство "Имя", необходимое для полиморфного вывода в строку"""
        pass

    def __str__(self):
        """Общая реализация отображения объекта в строке"""
        return f"{self.name} - {round(self.fabric_count, 2)} п.м. ткани"

    def __repr__(self):
        """Отображение объектов в строках при вложенных вызовах"""
        return self.__str__()

class Coat(Сlothes):
    """Класс "Пальто" для задания 2"""
    def __init__(self, volume: float):
        self._volume = volume

    @property
    def fabric_count(self):
        return self._volume / 6.5 + .5

    @property
    def name(self):
        return "Пальто"

class Suit(Сlothes):
    """Класс "Костюм" для задания 2"""
    def __init__(self, height: float):
        self._height = height

    @property
    def fabric_count(self):
        return self._height * 2 + .3

    @property
    def name(self):
        return "Костюм"

