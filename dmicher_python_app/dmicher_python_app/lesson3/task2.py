# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.

import datetime

users = [] # будет накапливать пользователей в ОЗУ, пока всё приложение не будет зарыто

def run():
    """Выполняет задачу 2 урока 3"""
    print("\r\nЗадание 2")

    # Заполняет базу данных
    while True:
        print("\r\nКоличество введённых пользователей = " + str(len(users)))

        # Вводить ли данные дальше?
        user_input = input("Ввести нового пользователя? (да = y, д или пустой ввод) (нет = q, n, й, н): ").lower()

        if user_input in ("q", "й", "n", "н"):
            print("Ввод данных завершён.")
            break

        if not user_input.isspace() and user_input not in ("", "д", "y"):
            print("Неожиданный ответ. Введите один из приемлемых вариантов ввода.")
            continue

        # Ввод данных о новом пользователе
        first_name = input("Введите имя пользователя [обязательное поле]: ")
        while first_name == "" or first_name.isspace():
            first_name = input("Имя - обязательное поле. Оно не должно быть пустым.\r\n" + 
                               "Пожалуйста, введите приемлемое имя: ")

        last_name = input("Введите фамилию пользователя [обязательно поле]: ")
        while last_name == "" or last_name.isspace():
            last_name = input("Фамилия - обязательное поле. Она не должно быть пустым.\r\n" + 
                               "Пожалуйста, введите приемлемую фамилию: ")

        birth_year = input("Введите год рождения (необязательно): ")
        if not birth_year.isdigit():
            birth_year = None
        else:
            birth_year = int(birth_year)
            while birth_year < 1900 or birth_year > datetime.datetime.today().year:
                birth_year = input("Вводимое значение года должно быть в диапазоне от 1900 и до текущего года.\r\n" + 
                                   "Введите приемлемое значние или оставьте поле пустым: ")
                if not birth_year.isdigit():
                    birth_year = None
                    break
                birth_year = int(birth_year)

        city = input("Введите город (необязательно): ")
        if city.isspace() or city == "":
            city = None
        email = input("Введите электронную почту (необязательно): ")
        if email.isspace() or email == "":
            email = None
        phone_number = input("Введите телефон (необязательно): ")
        if phone_number.isspace() or phone_number == "":
            phone_number = None

        user_add(last_name=last_name, phone_number=phone_number, first_name=first_name, email=email, birth_year=birth_year, city=city)

    # Выводит данные по каждому пользователяю одной строкой
    for user in users:
        message = "- "
        for key in user.keys():
            if user[key] is not None:
                message += f"{key}: {user[key]}. "
        print(message)

    print("Задание выполнено\r\n")

def user_add(first_name, last_name, birth_year = None, city = None, email = None, phone_number = None):
    """Добавляет информацию о пользователе в базу данных.
    :param first_name: имя пользователя -> str
    :param last_name: фамилия пользователя -> str
    :param birth_year: (опционально) год рождения -> int, None
    :param city: (опционально) город проживания -> str, None
    :param email: (опционально) электронная почта -> str, None
    :param phone_number: (опционально) телефон -> str, None
    :return: None
    :rtype: None
    """
    users.append({
                "Имя": first_name,
                "Фамилия": last_name,
                "Год рождения": birth_year,
                "Город": city,
                "Почта": email,
                "Телефон": phone_number
            })
