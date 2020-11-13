from abc import ABC, abstractmethod

class AbstractEquipment():
    """Базовый класс офисной техники"""
    name: str

    def __init__(self, name: str):
        """Инициирует объект начальными значениями"""
        self.name = name

    def __str__(self):
        """Строковое представление объекта (без настроек)"""
        return (self.name)

    def __repr__(self):
        """Представление объекта для вложенных типов"""
        return self.__str__()

    @abstractmethod
    def description(self):
        """Абстрактный метод, требующий от оборудования предоставить свой статус"""
        pass

class Printer(AbstractEquipment):
    """Класс "Принтер", подкласс офисной техники"""
    def __init__(self):
        """Конструктор класса добавляет слово `принтер` и передаёт родителю"""
        return super().__init__("Принтер")

    def description(self):
        """Имитирует уникальное поведение"""
        return "Я принтер. Могу печатать."

class Scanner(AbstractEquipment):
    """Класс "Сканер", подкласс офисной техники"""
    def __init__(self):
        """Конструктор класса добавляет слово `сканер` и передаёт родителю"""
        return super().__init__("Сканер")

    def description(self):
        """Имитирует уникальное поведение"""
        return "Я сканер. Могу сканировать."

class MultiFunctionalMacheene(AbstractEquipment):
    """Класс "МФУ", подкласс офисной техники"""
    def __init__(self):
        """Конструктор класса добавляет слово `сканер` и передаёт родителю"""
        return super().__init__("МФУ")

    def description(self):
        """Имитирует уникальное поведение"""
        return "Я МФУ. Могу и печатать, и сканировать, а ещё я факс и телефон."