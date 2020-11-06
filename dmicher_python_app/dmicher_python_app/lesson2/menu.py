import lesson2.task1 as t1, lesson2.task2 as t2, lesson2.task3 as t3, lesson2.task4 as t4
import lesson2.task5 as t5, lesson2.task6 as t6

# показывает меню уроку № 2
def show():
    while True:
        print("Урок № 2. Встроенные типы и операции с ними.")
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