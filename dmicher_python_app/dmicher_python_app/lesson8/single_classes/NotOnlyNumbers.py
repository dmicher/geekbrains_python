from tools import DmicherException, Tools as tools

class OnlyNumbersFactory():
    """Класс, призванный анализировать наличие в перечислениях элементов,
    отличных от числовых значений"""
    __result: list

    def __init__(self):
        self.__result = []
        pass

    def generate(self):
        """Пока пользователь продожает вводить данных (до ввода q) заполняет список
        приемлемым для этого вводом. О неприемлемом вводе сообщает"""
        self.__result.clear() # затирает на случай повторного использования
        while True:
            user_input = input("Введите число (q - завершить): ").lower().strip()

            if user_input in ('q', 'й'):
                return self.__result
            else:
                try:
                    self.__next_number(user_input)
                except NotNumberDmicherException as ex:
                    print(ex)

    def __next_number(self, num_string: str):
        """Проверяет полученную строку на приемлемость и, если  всё ок, добавляет 
        новый номер в результирующее перечисление. Если нет, кидается исключением
        NotNumberDmicherException"""
        num = tools.try_float(num_string.replace(',', '.'))
        if num is None:
            raise NotNumberDmicherException()

        self.__result.append(num)

class NotNumberDmicherException(DmicherException):
    """Исключение, возникающее при наличии в анализируемом перечислении
    данных, отличных от типа int, либо float"""
    def __init__(self):
        return super().__init__("Введённое значение не является числом.")