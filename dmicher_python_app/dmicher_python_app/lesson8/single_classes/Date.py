from tools import DmicherException

class Date():
    """Класс "Дата" для решения задачи 1"""
    __year: int
    __month: int
    __day: int

    def __init__(self, date_string: str):
        """Инициирует объект"""
        try:
            self.__day, self.__month, self.__year = Date._parce(date_string)
        except DmicherException as ex:
            raise DmicherException("Невозможно создать объект Date.\r\n\t" + ex.txt)

    @staticmethod
    def _parce(value: str):
        """Разбирает строку на значимые данные, возвращает кортеж в формате (d, m, y)"""
        parts = value.split('-')
        if len(parts) != 3:
            raise DmicherException("Неверный формат даты")

        for num in parts:
            if not num.isdigit():
                raise DmicherException("Значение [" + num + "] должно было быть числом.")

        day, month, year = [int(x) for x in parts]
        is_valid, message = Date._date_validation(day, month, year)

        if not is_valid:
            raise DmicherException("Неприемлемый формат даты. " + message)

        return (day, month, year)

    @classmethod
    def _date_validation(cls, day: int, month: int, year: int):
        """Проверяет валидность переданных данных (не учитывает особенности календаря)
        Возвращает флаг успешной проверки и сообщение об ошибке, если нужно"""
        if day < 1 or day > 31:
            return False, f"Значение [{day}] является недопустимым для даты. Диапазон от 1 до 31." 
        if month < 1 or month > 12:
            return False, f"Значение [{month}] является недопустимым для месяца. Диапазон от 1 до 12."
        if year < 1970 or year > 2030:
            return False, f"Значение [{year}] является недопустимым для года. Диапазон от 1970 до 2030." 
        return True, ''

    def __str__(self):
        """Возвращает собственое строковое представление"""
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __repr__(self):
        """Возвращает представление для вложенных типов"""
        return self.__str__