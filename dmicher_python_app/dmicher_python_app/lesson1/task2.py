# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def run():
    print("\r\nЗадание 2\r\n")

    seconds = input("Введите целое количество секунд: ")

    if not seconds.isdigit():
        print("Введённое значение не является целым положительным числом.")
        return None
    seconds = int(seconds)

    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print("Введённое время - {}:{}:{}".format(hours, minutes, seconds))
    print("Задание завершено.\r\n")
