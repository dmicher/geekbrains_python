import lesson4.task1 as t1, lesson4.task2 as t2, lesson4.task3 as t3, lesson4.task4 as t4
import lesson4.task5 as t5, lesson4.task6 as t6, lesson4.task7 as t7

def show():
    """показывает меню уроку № 3"""
    while True:
        print("Урок № 4. Полезные инструменты.")
        command = input("Введите номер задания от 1 до 6 (иное - выход): ")

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
            elif number == 6:
                t6.run()
            elif number == 7:
                t7.run()
            else:
               return None
        else:
            return None
