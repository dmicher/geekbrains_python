# 4. Пользователь вводит целое положительное число. 
# Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.

def run():
    """Выполняет задачу 4 домашнего задания к уроку 1"""
    print("\r\nЗадание 4\r\n")
    str1 = input("Введите целое положительное число: ")

    if not str1.isdigit():
        print("Введённое значение не является целым положительным числом.")
        return None

    chars = list(str1)
    iterator = 0
    max_value = 0
    while iterator < len(str1):
        cur_value = chars[iterator]
        if not cur_value.isdigit():
            continue
        cur_value = int(cur_value)
        if max_value < cur_value:
            max_value = cur_value
        iterator += 1

    print("Максимальная цифра в введённом числе = ", max_value)
    print("Задание завершено.\r\n")