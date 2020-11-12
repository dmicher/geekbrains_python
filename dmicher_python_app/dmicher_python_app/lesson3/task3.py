# Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.

from tools import Tools as tools

def run():
    """Выполняет задачу _ урока 3"""
    print("\r\nЗадание 3\r\n")
    
    while True:
        user_input = input("Введите 3 призвольных вещественных числа через пробел (пустой ввод - выход): ")

        if user_input == "" or user_input.isspace():
            print("Ввод данных завершён.")
            break;

        params = user_input.split()
        if len(params) < 3:
            print("Вы ввели меньше трёх чисел. Расчёт не проведён.")
            continue

        if len(params) > 3:
            print("Вы ввели больше трёх чисел. Лишние значения были проигнорированы.")

        result = my_func(params[0], params[1], params[2])

        if result is None:
            print("Расчёт отменён.")
            continue

        print("Сумма двух наибольших чисел из введённых Вами =", str(result))

    print("Задание завершено\r\n")

def my_func(a, b, c):
    """Возвращает сумму двух наибольших из трёх передаваемых параметров
    :param a: потенциальное слагаемое a -> float, int, str(float)
    :param b: потенциальное слагаемое b -> float, int, str(float)
    :param c: потенциальное слагаемое c -> float, int, str(float)
    :return: Сумма двух наибольших чисел
    :rtype: float
    """

    # Контроль приемлемости данных и попытка привести их к числу
    params = [a, b, c]
    for index in range(len(params)): # итерирует по индексам, чтобы перезаписывать элементы
        if type(params[index]) != float:
            if type(params[index]) == int:
                params[index] = float(params[index])
            elif type(params[index]) == str:
                params[index] = tools.try_float(params[index])

            if type(params[index]) != float:
                print("Ошибка формата данных. Не все введённые параметры являются числами.")
                return None

    # поиск наибольших значений
    params.sort(reverse=True)
    return params[0] + params[1]

