# 6. Спортсмен занимается ежедневными пробежками. 
# В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

import tools

def run():
    """Выполняет задачу 6 домашнего задания к уроку 1"""
    print("\r\nЗадание 6\r\n")
    
    current_distance = input("Введите начальную дистанцию: ").replace(',', '.')
    if not tools.is_float(current_distance):
        print("Значение дистанции должно быть числовым")
        return None
    current_distance = float(current_distance)
    if current_distance <= 0:
        print("Значение дистанции должно быть больше нуля")

    aim_distance = input("Введите целевую дистанцию: ").replace(',', '.')
    if not tools.is_float(aim_distance):
        print("Значение дистанции должно быть числовым")
        return None
    aim_distance = float(aim_distance)
    if aim_distance < current_distance:
        print("Целевая дистанция не должны быть меньше начальной дистанции")
        return None

    current_day = 0
    while current_distance < aim_distance:
        current_day += 1
        current_distance += current_distance * 0.1

    print(f"Ответ: на {current_day}-й день спортсмен достиг результата — не менее {aim_distance} км.")
    print("Задание завершено.\r\n")