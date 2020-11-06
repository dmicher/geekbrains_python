import lesson1.menu as l1, lesson2.menu as l2

def main_menu(show_hello):
    """Выводит главное меню на экран"""
    if (show_hello):
        print("Добро пожаловать в программу.")
        print("Выберите пункт меню.")
        print()
    print("ОСНОВНОЕ МЕНЮ:")
    print("\t1\t= Урок 1: Знакомство с Python.")
    print("\t2\t= Урок 2: Встроенные типы и операции с ними.")
    print()
    print("\tв, q\t= выход\r\n")
    print("\tа, v\t= о программе\r\n")

# Точка входа
main_menu(True)
while True:
    command = input("Введите номер урока: ")
    if command.isdigit():
        number = int(command)
        if number == 1:
            l1.show()
        elif number == 2:
            l2.show()
        else:
           continue
    elif command == "в" or command == "q" or command == "й" or command == "d":
        print("До свидания.")
        break
    elif command == "а" or command == "f" or command == "v" or command == "м":
        print("Автор: dmicher abathur kubrow (Черкасов Д.С.)\r\nВерсия: 2.0")
    else:
        main_menu(False)