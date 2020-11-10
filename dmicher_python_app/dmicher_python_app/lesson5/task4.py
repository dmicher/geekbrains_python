# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных 
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import tools, os

def run():
    """Выполняет задание 4 урока 6"""
    print("\r\nЗадание 4\r\n")

    user_input = input("Введите набор целых положительных чисел, разделяя их пробелами (другие данные будут прогнорированы):\r\n> ")

    numbers = [int(x) for x in user_input.split() if x.isdigit()]

    file_path = os.path.join(tools.get_dir(), "lesson5_task4.txt")

    with open(file_path, 'w') as stream:
        print(*numbers, file=stream)

    print("Ваш массив данных размещён в файле:\r\n" + file_path)
    print("Сумма введённых чисел: " + str(sum(numbers)))
    tools.ask_to_read_file(file_path)

    print("Задение выполнено\r\n")

