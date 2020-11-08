import lesson3.task1 as t1, lesson3.task2 as t2, lesson3.task3 as t3, lesson3.task4 as t4
import lesson3.task5 as t5, lesson3.task6 as t6

def show():
    """показывает меню уроку № 3"""
    while True:
        print("Урок № 3. Функции.")
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
            else:
               return None
        else:
            return None
