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

def ask_to_read_file(path: str, forced_UTF8: bool=False):
    """Спрашивает пользователя, нужно ли читать файл, указанный в параметре и,
    если нужно, выводит содержимое в консоль.
    :param path: путь к файлу (не проверяет его существование)
    :param forced_UTF8: прочитать принудительно в кодировке UTF-8
    :return: ничего не возвращает"""
    
    user_input = input("\r\nПрочесть файл? (да = y, д, пустой ввод) (нет = иное)").lower().strip()
    if user_input in ('y', 'д', ''):
        try:
            print("---содержимое файла---")
            if forced_UTF8:
                with open(path, encoding='utf8') as stream:
                    print(stream.read())
            else:
                with open(path) as stream:
                    print(stream.read())
            print("------конец файла-----")
        except BaseException as ex:
            print("Ошибка чтения файла", ex)

class DmicherException(Exception):
    """Исключения, пораждаемые в этом проекте"""
    def __init__(self, text):
        self.txt = text