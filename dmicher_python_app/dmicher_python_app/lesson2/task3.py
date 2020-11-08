# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

def run():
    """Выполняет задачу 3 домашнего задания к уроку 2"""
    print("\r\nЗадание 3\r\n")

    # простой список: индекс = номер месяца месяц без единицы
    print("Реализация 1. Список\r\n")

    month = get_month()
    if month == None:
        return

    year_times_list = ["январь - зимний", "февраль - зимний", "март - весенний", "апрель - весенний", "май - весенний", 
                       "июнь - летний", "июль - летний", "август - летний", "сентябрь - осенний", 
                       "октябрь - осенний", "ноябрь - осенний", "декабрь - зимний"]
    print("Введённый Вами месяц - это", year_times_list[month - 1], "месяц.\r\n")

    # реализация через словарь: ключ = номер месяца
    print("Реализация 2. Словарь\r\n")

    month = get_month()
    if month == None:
        return

    year_times_dictionary = {1: "январь - зимний", 2: "февраль - зимний", 3: "март - весенний", 
                             4: "апрель - весенний", 5: "май - весенний", 6: "июнь - летний", 
                             7: "июль - летний", 8: "август - летний", 9: "сентябрь - осенний", 
                             10: "октябрь - осенний", 11: "ноябрь - осенний", 12: "декабрь - зимний"}
    print("Введённый Вами месяц - это", year_times_dictionary[month], "месяц.")
    print("Задание завершено\r\n")

def get_month():
    """Получает у пользователя интересующий его номер месяца. Возвращает int при успехе или None, если что-то пошло не так"""
    month_number = input("Введите номер месяца (от 1 до 12):")

    if not month_number.isdigit():
        print("Неприемлемый ввод. Номер месяца должен быть целым цислом.")
        return None

    month_number = int(month_number)
    if month_number < 1 or month_number > 12:
        print("Неприемлемый ввод. Номер месяца должен быть от 1 до 12.")
        return None

    return month_number
