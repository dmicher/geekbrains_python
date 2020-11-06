# Проверяет, является ли строка представление числа с плавающей точкой
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
