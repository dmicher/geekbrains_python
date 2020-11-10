# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и 
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет 
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней 
# величины дохода сотрудников.
# Пример файла:
#   Иванов 23543.12 
#   Петров 13749.32
# Создать (не программно) текстовый файл со следующим содержимым:
#   One — 1
#   Two — 2
#   Three — 3
#   Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно 
# данные. При этом английские числительные должны заменяться на русские. Новый блок 
# строк должен записываться в новый текстовый файл.

import tools, os

def run():
    """Выполняет задание 3 урока 6"""
    print("\r\nЗадание 6\r\n")

    # Часть 1 - Зарплата сотрудников
    print("Часть 1 - Зарплата сотрудников")
    directory = tools.get_dir("lesson5_data")

    if directory is None:
        print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")
        return

    file = os.path.join(directory, "task3a_data.txt")
    if not os.path.exists(file) or not os.path.isfile(file):
        print("Файл с указанным именем не обнаружен, либо не является файлом." + 
              "Проверьте, что Вы загрузили все файлы проекта.")
        return
    
    strings = []
    try:
        with open(file) as stream:
            strings = stream.readlines()
    except:
        print("Ошибка чтения файла")
        return
    
    persons = {line.split(' ')[0]: float(line.split(' ')[1]) for line in strings if line != ''}

    print("Оклад меньше 20 тыс. у следующих сотрудников: ", *[person for person in persons.keys() if persons[person] < 20_000])
    print("Средняя заработная плата: " + str(round(sum(persons.values()) / len(persons), 2)))

    # Часть 2 - Числительные
    print("Часть 2 - Числительные")
    
    dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть",
                  "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Zero": "Ноль"}

    in_file = os.path.join(directory, "task3b_data.txt")
    if not os.path.exists(file) or not os.path.isfile(file):
        print("Файл с указанным именем не обнаружен, либо не является файлом." + 
              "Проверьте, что Вы загрузили все файлы проекта.")
        return
    
    directory = tools.get_dir()
    if directory is None:
        print("Ошибка создания директории для хранения новых фалов.")
        return

    out_file = os.path.join(directory, "lesson5_task3.txt")
    try:
        with open(in_file) as in_stream:
            with open(out_file, 'w') as out_stream:
                while True:
                    line = in_stream.readline()
                    if not line:
                        break
                    word_to_replace = line.split('-')[0].strip()
                    out_stream.write(line.replace(word_to_replace, dictionary[word_to_replace]))
    except BaseException as ex:
        print("Ошибка чтения или записи файлов", ex)
        return

    print("Новый файл с переводом опубликован по следующему пути\r\n" + out_file)
    user_input = input("\r\nПрочесть файл? (да = y, д, пустой ввод) (нет = иное)").lower().strip()

    if user_input in ('y', 'д', ''):
        try:
            print("---содержимое файла---")
            with open(out_file) as stream:
                print(stream.read())
            print("------конец файла-----")
        except:
            print("Ошибка чтения файла")

    print("Задение выполнено\r\n")

