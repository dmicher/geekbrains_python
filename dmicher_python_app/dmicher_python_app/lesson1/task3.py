# 3.  Узнайте у пользователя число n.  Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.  Считаем 3 + 33 + 333 = 369.
def run():
    print("\r\nЗадание 3\r\n")
    
    int1 = input("Введите целое положительное число: ")

    if not int1.isdigit():
        print("Введённое значение не является целым положительным числом.")
        return None

    single = int(int1)
    double = int(int1 + int1)
    triple = int(int1 + int1 + int1)

    print(f"{single} + {double} + {triple} = {single + double + triple}")
    print("Задание завершено.\r\n")