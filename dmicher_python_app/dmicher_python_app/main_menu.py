import lesson1.menu as l1

# Выводит главное меню на экран
def main_menu(show_hello):
    if (show_hello):
        print("Добро пожаловать в программу.")
        print("Выберите пункт меню.")
        print()
    print("ОСНОВНОЕ МЕНЮ:")
    print("\t1\t= Урок 1: Знакомство с Python.")
    print()
    print("\tв, q\t= Выход\r\n")

# Точка входа
main_menu(True)
while True:
    command = input("Введите номер урока: ")
    if command.isdigit():
        number = int(command)
        if number == 1:
            l1.show()
        else:
           continue
    elif command == "в" or command == "q" or command == "й" or command == "d":
        print("До свидания.")
        break
    else:
        main_menu(False)