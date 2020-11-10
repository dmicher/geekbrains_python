# Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

import tools, os, re

def run():
    """Выполняет задание 2 урока 6"""
    print("\r\nЗадание 6\r\n")
    
    path = tools.get_dir("lesson5_data")
    if path is None:
        print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")
        return

    path = os.path.join(path, "task2_toread.txt")
    if not os.path.exists(path) or not os.path.isfile(path):
        print("Файл с указанным именем не обнаружен, либо не является файлом." + 
              "Проверьте, что Вы загрузили все файлы проекта.")
        return

    strings = []
    try:
        with open(path) as stream:
            strings = stream.readlines()
    except:
        print("Ошибка чтения файла")
        return
    
    # Теперь немного "магии одной строки". 
    # Следующая команда последовательно:
    # - берёт каждую прочитанную строку, если она пустая, то пропускает её, а для остальных:
    #       - удаляет пробельные символы в начале и конце строки;
    #       - удаляет все символы, не являющиеся пробельными либо буквами латиницы и кириллицы;
    #       - из полученной строки удаляет задублированные пробелы. Они могут появляться, после
    #           предыдущей команды при удалении тире ('_-_' -> '__');
    #       - считает количество пробелов, разделяющих слова, и добавляет единицу - это количество слов;
    #       - добавляет полученную строку в перечисление кортежей, где первую часть занимает посчитанное количество слов, 
    #           а во второй части находится исходная строка;
    # - сформированное перечисление кортежей пронумировывает (начиная со значения 1) и передаёт в словарь, где 
    #     ключом выступает номер строки, а значением - вышеуказанный кортеж из строки и количества слов в этой;
    magic = {string_num: line for string_num, line 
           in enumerate(((re.sub(r"[^a-zA-ZА-Яа-я\s]", '', line.strip()).replace('  ', ' ').count(' ') + 1, line) 
                         for line in strings if not line.isspace() and line != ''), start=1)}
    
    # осталось только красиво вывести на экран
    print("Стр.№", "Кол.", "Строка", sep="\t| ")
    print('-'*30)
    for key, value in magic.items():
        print(key, value[0], value[1].replace("\n", ''), sep="\t| ")

    print("Задение выполнено\r\n")

