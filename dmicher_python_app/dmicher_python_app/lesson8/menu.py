import lesson8.task1 as t1, lesson8.task2 as t2, lesson8.task3 as t3
import lesson8.task4_6 as t4, lesson8.task7 as t7

def show():
    """показывает меню уроку № 6"""
    while True:
        print("Урок № 8. ООП. Полезные дополнения.")
        command = input("\r\nВведите номер задания от 1 до 7\r\n   (4-6 - одно и тоже; иное - выход): ")

        if command.isdigit():
            number = int(command)
            if number == 1:
                t1.run()
            elif number == 2:
                t2.run()
            elif number == 3:
                t3.run()
            elif number in (4, 5, 6):
                t4.run()
            elif number == 7:
                t7.run()
            else:
               return None
        else:
            return None
