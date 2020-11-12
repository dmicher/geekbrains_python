# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

from tools import Tools as tools

def run():
    """Выполняет задачу 1 урока 3"""
    print("\r\nЗадание 1\r\n")
    while True:
        command = input("Введите два вещественных чила (A и B), разделив их пробелом (q или й - выход): ")
        
        if command.lower() in ("q", "й"):
            break

        numbers = command.split()
        
        if len(numbers) < 2:
            print("Введено недостаточное количество параметров. Расчёт прерван.")
            continue
        
        if len(numbers) > 2:
            print("Введено избыточное количество параметров. Лишние будут проигнорированы.")

        result = double_division(numbers[0], numbers[1])

        if result is None:
            print("Операция прервана")
            continue

        res1 = round(result[0], 4) if result[0] is not None else "[деление на ноль]"
        res2 = round(result[1], 4) if result[1] is not None else "[деление на ноль]"
        print(f"Результаты деления: A / B = {res1}; B / A = {res2}")

    print("Задание завершено\r\n")

def double_division(a, b):
    """Проводит деление двух чисел между собой. Возвращает два результата: деление a на b и деление b на a.
    Если деление невозможно (деление на ноль), возвращает None.

    :param a: первое число -> str, int, float
    :param b: второе число -> str, int, float
    :return: кортеж (res1, res2) с результатом деления -> float, None
    """

    # проверяет приемлемость введённых данных
    if type(a) == str:
        a = tools.try_float(a)
        if a is None:
            print("Неприемлемый ввод. Переменная 'A' не является числом.")
            return None

    if type(a) == int:
        a = float(a)

    if type(a) != float:
        print("Неприемлемый ввод. Переменная 'A' имеет неприемлемый формат.")
        return None

    if type(b) == str:
        b = tools.try_float(b)
        if b is None:
            print("Неприемлемый ввод. Переменная 'B' не является числом.")
            return None

    if type(b) == int:
        b = float(b)

    if type(b) != float:
        print("Неприемлемый ввод. Переменная 'B' имеет неприемлемый формат.")
        return None

    # высчитывает деление, выдаёт результат
    return a / b if b != 0 else None, b / a if a != 0 else None
