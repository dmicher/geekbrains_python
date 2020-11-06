def is_float(string):
    """Проверяет, является ли строка представление числа с плавающей точкой"""
    try:
        float(string)
        return True
    except ValueError:
        return False
