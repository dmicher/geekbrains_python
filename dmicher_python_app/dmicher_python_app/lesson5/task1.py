# Создать программно файл в текстовом формате, записать в него построчно данные, 
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

import os, tools

def run():
    """Выполняет задание 1 урока 6"""
    print("\r\nЗадание 6\r\n")

    user_input = input("Начните вводить данные. Пустой ввод - отмена (завершение) ввода." +
                      "Запись в файл произойдёт после завершения ввода.\r\n> ")
    strings = []

    while user_input != '' and not user_input.isspace():
        strings.append(user_input + "\n")
        user_input = input("> ")

    file_path = os.path.join(tools.get_dir(), "lesson5_task1.txt")

    try:
        with open(file_path, 'wt') as stream:
            stream.writelines(strings)
    except:
        print("Ошибка записи в файл")
        return

    user_input = input("Запись в файл успешна. Прочесть файл? (да = y, д, пустой ввод) (нет = иное)").lower().strip()

    if user_input in ('y', 'д', ''):
        try:
            print("---содержимое файла---")
            with open(file_path) as stream:
                print(stream.read())
            print("------конец файла-----")
        except:
            print("Ошибка чтения файла")

    print("Задение выполнено\r\n")
