class WarehouseException(Exception):
    """Исключительные ситуации, возникающие при работе офисного склада"""
    def __init__(self, text: str):
        self.txt = text

    def __str__(self):
        """Строковое представление этой ошибки"""
        return "Ошибка склада: " + self.txt

    def __repr__(self):
        """Представление во вложенных типах"""
        return self.__str__()


