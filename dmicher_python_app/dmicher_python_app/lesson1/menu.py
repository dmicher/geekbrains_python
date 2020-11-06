import lesson1.task1 as t1, lesson1.task2 as t2, lesson1.task3 as t3, lesson1.task4 as t4, lesson1.task5 as t5, lesson1.task6 as t6

# показывает меню урока
def show():
    while True:
        print("Урок № 1. Знакомство с Python.")
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