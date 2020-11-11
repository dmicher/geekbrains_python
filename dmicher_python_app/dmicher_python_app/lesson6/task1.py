# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) 
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать 
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния 
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше 
# усмотрение. Переключение между режимами должно осуществляться только в указанном порядке 
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить 
# соответствующее сообщение и завершать скрипт.

import tools, time
from lesson6.TrafficLight import TrafficLight

def run():
    """Демонстрирует работу классов для задания 1 в уроке 6"""
    print("\r\nЗадание 1\r\n")

    # Инструкция по применению
    print("Этот скрипт позволяет следить за светофором и настраивать его поведение. ")
    print("Вы можете ввести ряд параметров, которые будут выполнены светофором.")
    print("Если Вы не введёте никаких команд, светофор отработает в значениях \"по умолчанию\".")
    print("\r\nДоступны следующие команды (любую из них можно пропустить):")
    print("\ttime=40.1\t - общее время работы светофора - 40.1 секунд;")
    print("\tchange=3.2,y,1.2 - через 3.2 секунды на светофор поступит команда на изменение его настроек:" + 
                  "\r\n\t\t\t   для y=жёлтого/r=красного/g=зелёного света будет задана новая продолжительность." +
                  "\r\n\t\t\t   Настройка вступит в силу на следующий раз, когда загорится указанный свет." + 
                  "\r\n\t\t\t   Этот параметр допустимо указать несколько раз для разных времени и светов.")
    print("\tupdate=0.1\t - период (в секундах) обновления статуса светофора в в консоли.")
    print("Пример команды:\r\n\ttime=120 update=0.2 change=30.2,y,1.2 change=12,r,3 change=20,g,4")
    user_input = input("\r\nВведите команду или пустую строку: ")

    # Получает и анализирует команду пользователя
    commands = {}
    if user_input:
        for key, value in (command.split('=') for command in user_input.split()):
            try:
                if key not in ("time", "change", "update"):
                    continue
                if key == "time":
                    commands["time"] = round(float(value), 2)
                elif key == "update":
                    commands["update"] = round(float(value), 2)
                elif key == "change":
                    change_time, color, new_color_time = value.split(',')

                    change_time = tools.try_float(change_time)
                    if not change_time:
                        continue

                    colors_dict = {"y": "жёлтый", "r": "красный", "g": "зелёный"}
                    if color not in ("y", "r", "g"):
                        continue
                    color = colors_dict[color]
                    
                    new_color_time = tools.try_float(new_color_time)
                    if not new_color_time:
                        continue

                    if "changes" in commands:
                        commands["changes"].append((change_time, color, new_color_time))
                    else:
                        commands["changes"] = [(change_time, color, new_color_time)]
            except:
                print("Ошибка формата строки параметров. Работа остановлена.")
                return
            else:
                continue
    else:
        commands = {
            "changes": [
                (30.0, "жёлтый", 1.0),
                (12.0, "зелёный", 10.0)
                ]
            }

    if "time" not in commands:
        commands["time"] = 60.0
    if "update" not in commands:
        commands["update"] = .1
    commands["changes"].sort(key=lambda x: x[0])

    # Параметры запуска
    print("Параметры запуска светофора:")
    print("Общее время работы: " + str(commands["time"]) + ". Частота обновления: " + str(commands["update"]))
    print("Продолжительность света при старте:" +
          "\r\n\t- красный 7 с.,\r\n\t- жёлтый 2 с.,\r\n\t- зелёный 14 с.")
    if "changes" in commands:
        print("Изменения в продолжительности света:")
        for change_time, color, change in commands["changes"]:
            print("\t- после " + str(change_time) + " с. " + color + " свет будет зажигаться на " + str(change) + " c." )
    else:
        print("Изменений в продолжительности света нет.")

    # Работа светофора
    start_time = time.time()
    traffic_light = TrafficLight()
    print("\r\nСветофор включен.")
    while commands["time"] - time.time() + start_time > 0:
        # проверяет, настало ли время менять продолжительность светов (по настройкам); если да - меняет их
        time_passed = time.time() - start_time;
        for change in (command for command in commands["changes"] if command[0] <= time_passed):
            _, color, new_time = change
            commands["changes"].remove(change)
            traffic_light.set_color_time(color, new_time)
            print(color.capitalize() + " свет теперь будет гореть " + str(round(new_time, 2)) + " c." + (" " * 40))

        # статистика по текущему свету и общей работе светофора
        color, color_time_left = traffic_light.running()
        print("Свет " + color.upper() + "\t" + str(round(color_time_left, 2)) +
              "\tСветофор работает " + str(round(time_passed, 2)) +
              "\tвыключится " + str(round(commands["time"] - time_passed, 2)) + (" " * 20), end='\r')

        # освобождает ресурсы компьютера на установленный период обновления
        time.sleep(commands["update"])

    # Ура, конец
    print("Светофор выключен." + (" " * 80))
    print("\r\nЗадание завершено\r\n")