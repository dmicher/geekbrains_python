# Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также 
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить 
# ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json, os, tools

def run():
    """Выполняет задание 6 урока 6"""
    print("\r\nЗадание 6\r\n")

    path = tools.get_dir("lesson5_data")
    if path is None:
        print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")
        return

    path = os.path.join(path, "task6_data.txt")
    if not os.path.exists(path) or not os.path.isfile(path):
        print("Файл с данным для этого задания не обнаружен.\r\n" + path +
              "\r\nПроверьте, что Вы загрузили все файлы проекта.")
        return

    organizations = {}
    
    with open(path) as stream:
        while True:
            line = stream.readline()
            if not line:
                break

            parts = line.split()
            if len(parts) != 4:
                print("Неверный размер строки: " + line)
                continue

            name = parts[1] + " \"" + parts[0].replace('_', ' ') + "\""
            revenue = tools.try_float(parts[2])
            costs = tools.try_float(parts[3])

            if revenue is None:
                print("Неверное значение выручки в строке: " + line)
                continue
            if costs is None:
                print("Неверное значение расходов в строке: " + line)
                continue

            profit = round(revenue - costs, 2)
            
            if profit > 0:
                print(name, "работает с прибылью в", str(profit))

            organizations[name] = profit

    avarage_profit = str(round(sum(organizations.values()) / len(organizations), 2))
    print("Среднее значение прибыли (для прибыльных организаций):", avarage_profit)

    object_to_write = (organizations, {"avarage_profit": avarage_profit})
    path = os.path.join(tools.get_dir(), "lesson5_task6.json")

    try:
        with open(path, 'w', encoding='utf8') as stream:
            json.dump(object_to_write, stream, ensure_ascii=False)
    except BaseException as ex:
        print("Провал записи результирующего файла. " + ex)
        return

    print("Результирующий файл выгружен по пути:\r\n" + path)
    tools.ask_to_read_file(path, True)

    print("Задение выполнено\r\n")

