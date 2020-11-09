# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел,
# начиная с 1!  и до n!.

# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4!  = 1 * 2 * 3 * 4 = 24.

def run():
    """Выполняет задание 7 для урока № 4"""
    print("\r\nЗадание 7\r\n")

    user_input = input("Укажите, факториал скольких первых чисел Вы хотите получить (1 - 99): ")

    if not user_input.isdigit:
        print("Неверный формат ввода. Количество чисел должно быть целым положительным числом.")
        return

    count = int(user_input)
    if count < 1:
        print("Неверный формат ввода. Количество чисел должно быть не меньше единицы.")
        return
    if count > 99:
        print("Неверный формат ввода. Количество чисел не должно превышать 99 единиц.")
        return

    for i, el in fact(count):
        print((str(i) if i > 9 else "0" + str(i)) + "! =", el)

def fact(count: int):
    """Генератор ряда 'Факториал натуральных чисел': выдаёт несколько первых чисел ряда n!,
    где n - номер в последовательности.
    :param count: количество чисел, выдаваемых в последовательности -> int
    """
    current_factorial = 1
    for i in range(1, count + 1):
        current_factorial *= i
        yield i, current_factorial