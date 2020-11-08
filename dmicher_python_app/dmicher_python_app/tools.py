def is_float(string):
    """Проверяет, является ли строка представление числа с плавающей точкой"""
    try:
        float(string.replace(',', '.'))
        return True
    except ValueError:
        return False

def try_float(string):
    """Пытается преобразовать строку в тип float. При провале возвращает None
    :param string: преобразуемая строка
    :return: полученное число
    :rtype float, None
    """
    try:
        return float(string.replace(',', '.'))
    except:
        return None