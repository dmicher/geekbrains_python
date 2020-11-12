import lesson7.task1 as t1, lesson7.task2 as t2, lesson7.task3 as t3

def show():
    """показывает меню уроку № 6"""
    while True:
        print("Урок № 7. ООП. Продвинутый уровень.")
        command = input("Введите номер задания от 1 до 3 (иное - выход): ")

        if command.isdigit():
            number = int(command)
            if number == 1:
                t1.run()
            elif number == 2:
                t2.run()
            elif number == 3:
                t3.run()
            else:
               return None
        else:
            return None
