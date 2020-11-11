import lesson6.task1 as t1, lesson6.task2 as t2, lesson6.task3 as t3, lesson6.task4 as t4
import lesson6.task5 as t5

def show():
    """показывает меню уроку № 6"""
    while True:
        print("Урок № 6. Объектно-ориентированное программирование.")
        command = input("Введите номер задания от 1 до 5 (иное - выход): ")

        if command.isdigit():
            number = int(command)
            if number == 1:
                t1.run()
            elif number == 2:
                t2.run()
            elif number == 3:
                t3.run()
            elif number == 4:
                t4.run()
            elif number == 5:
                t5.run()
            else:
               return None
        else:
            return None
