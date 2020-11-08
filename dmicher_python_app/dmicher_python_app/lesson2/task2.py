# 2. Для списка реализовать обмен значений соседних элементов, т.е. 
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

def run():
    """Выполняет задачу 2 домашнего задания к уроку 2"""
    print("\r\nЗадание 2\r\n")

    user_input = input("Введите первое значение последовательности (строка), либо последовательность значений, разделённых пробелом: ")

    values = []
    if user_input.count(' ') < 1:
        values.append(user_input)
        while True:
            print("Текущая последовательность: ", values)
            user_input = input("Введите следующее значение (введите '!' для завершения ввода): ")
            if user_input == "!":
                break
            values.append(user_input)
    else:
        values = user_input.split(' ')

    if len(values) < 2:
        print("В последовательности недостаточно элементов для того, чтобы произвести хотя бы одну перестановку.")
        return

    print("Введённая последовательность: ", values)
    last_exchange_number = len(values) - 2 if len(values) % 2 == 0 else len(values) - 3

    iterator = 0
    while iterator <= last_exchange_number:
        values[iterator], values[iterator + 1] = values[iterator + 1], values[iterator]
        iterator += 2

    print("Перемешанная последовательность: ", values)
    print("Задание завершено\r\n")