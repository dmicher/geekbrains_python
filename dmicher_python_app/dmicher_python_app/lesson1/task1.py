# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите 
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

def run():
    print("\r\nЗадание 1\r\n")
    user_name = input("Введите Ваше имя: ")
    print(f"Здравствуйте, {user_name}!\r\n")

    int1 = input("Введите целое число: ")
    int2 = input("И ещё одно целое число: ")

    if not int1.isdigit() or not int2.isdigit():
        print("Как минимум одно из введённых Вами значений - не целое число.")
        return None
    
    int1 = int(int1)
    int2 = int(int2)
    print(f"{int1} + {int2} = {int1 + int2}")
    print(f"{int1} - {int2} = {int1 - int2}")
    print(f"{int2} - {int1} = {int2 - int1}")
    print(f"{int1} * {int2} = {int1 * int2}")
    if int2 == 0:
        print(f"{int1} / {int2} - недопустимо")
    else:
        print(f"{int1} / {int2} = {float(int1) / int2:2f}")
    if int2 == 0:
        print(f"{int2} / {int1} - недопустимо")
    else:
        print(f"{int2} / {int1} = {float(int2) / int1:2f}")
    print("Задание завершено.\r\n")