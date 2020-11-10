import os

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

def get_dir(subdir_name: str = 'tmp'):
    """Возвращает абсолютный путь к папке для хранения данных.
    Обеспечивает существование этой директории.
    (подпапка по умолчанию 'tmp' игнорируется в .gitignore)

    :param subdir_name: 
    :return: строку с путём к папке или None, если директория не создана
    :rtype bool, None
    """
    data_dir = './data_dir'
    if not enshure_dir_exist(data_dir):
        return None

    data_dir = os.path.join(os.path.abspath(data_dir), subdir_name)
    if enshure_dir_exist(data_dir):
        return data_dir
    return None

def enshure_dir_exist(path: str):
    """Обеспечивает существование указанной директории
    :param path: Путь для выбранной папки -> str
    :return: Флаг существования папки в результате выполнения функции
    :rtype: bool
    """
    if os.path.exists(path):
        if os.path.isdir(path):
            return True
        try:
            os.remove(path)
            os.mkdir(path)
            return True
        except:
            return False
    else:
        try:
            os.mkdir(path)
            return True
        except:
            return False