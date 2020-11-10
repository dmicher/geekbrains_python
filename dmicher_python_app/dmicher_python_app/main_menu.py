import lesson1.menu as l1, lesson2.menu as l2, lesson3.menu as l3, lesson4.menu as l4, lesson5.menu as l5

def main_menu(show_hello):
    """Выводит главное меню на экран"""
    if (show_hello):
        print("Добро пожаловать в программу.")
        print("Выберите пункт меню.")
        print()
    print("ОСНОВНОЕ МЕНЮ:")
    print("\t1\t= Урок 1: Знакомство с Python.")
    print("\t2\t= Урок 2: Встроенные типы и операции с ними.")
    print("\t3\t= Урок 3: Функции.")
    print("\t4\t= Урок 4: Полезные инструменты.")
    print("\t5\t= Урок 5: Работа с файлами.")
    print()
    print("\tв, q\t= выход")
    print("\tа, v\t= о программе")
    print("\tп, h\t= подсказка\r\n")

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
        elif number == 3:
            l3.show()
        elif number == 4:
            l4.show()
        elif number == 5:
            l5.show()
        else:
           continue
    elif command in ("в", "q", "й", "d"):
        print("До свидания.")
        break
    elif command in ("а", "f", "v", "м"):
        print("Автор: dmicher abathur kubrow (Черкасов Д.С.)\r\nВерсия: 5.0")
    elif command in ("h", "g", "р", "п"):
        print("Эта программа демонстрирует выполненные всех домашних заданий по курсу \"Введиение в Python\".\r\n" +
              "Для навигации по меню программы вводите в меню номеры соответствующих уроков и задач.\r\n" +
              "После того, как Вы выберите конкретную задачу, управление будет передано модулю, выполняющему задание. " + 
              "После выполнения задания управление будет возвращено в меню выбранного урока. Чтобы попасть обратно в главное меню, " + 
              "следуйте указаниям в выводе меню уроков.\r\n")
    else:
        main_menu(False)