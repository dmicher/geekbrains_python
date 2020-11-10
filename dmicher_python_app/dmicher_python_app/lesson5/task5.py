# Необходимо создать (не программно) текстовый файл, где каждая строка описывает 
# учебный предмет и наличие лекционных, практических и лабораторных занятий по 
# этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее 
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
#    Информатика: 100(л) 50(пр) 20(лаб).
#    Физика: 30(л) — 10(лаб)
#    Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import tools, os

def run():
    """Выполняет задание 5 урока 6"""
    print("\r\nЗадание 5\r\n")

    path = tools.get_dir("lesson5_data")
    if path is None:
        print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")
        return

    path = os.path.join(path, "task5_data.txt")
    if not os.path.exists(path) or not os.path.isfile(path):
        print("Файл с данным для этого задания не обнаружен.\r\n" + path +
              "\r\nПроверьте, что Вы загрузили все файлы проекта.")
        return

    strings = []
    with open(path) as stream:
        strings = stream.readlines()

    # Парсирует строку в 2 этапа:
    # - сначала, создаёт словарь, игнорируя невалидные строки в файле;
    # - затем заменяет строковые значения в словаре на словари "тип занятия": "количество часов", заодно подменяя условное обозначение именем занятия
    dictionary = {pair[0].strip(): pair[1].strip() for pair in (line.split(': ') for line in strings if line) if len(pair) == 2}
    names = {"лаб)": "Лабораторная работа", "л)": "Лекция", "пр)": "Практические занятия"}
    for key in dictionary.keys():
        dictionary[key] = {names[pair[1]]: int(pair[0]) for pair in (parts.split('(') for parts in dictionary[key].split()) if len(pair) == 2}

    print("Всего занятий: ")
    print("- по предметам:", *(f" {key}-{sum} ч." for key, sum in {(key, sum(dictionary[key].values())) for key in dictionary.keys()}))

    # бонусом (от того, что типы занятий не отброшены, а также были парсированы): по типам занятий
    by_types = {}
    for item in dictionary.values():
        for key in item.keys():
            if key in by_types:
                by_types[key] += item[key]
            else:
                by_types[key] = item[key]

    print("- по типам занятий:", *(f" {key}-{by_types[key]} ч." for key in by_types.keys()))
    print("Задение выполнено\r\n")