# 4 Начните работу над проектом Склад оргтехники. Создайте класс, описывающий склад. 
#   А также класс Оргтехника, который будет базовым для классов-наследников. 
#   Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
#   В базовом классе определить параметры, общие для приведенных типов.
#   В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём 
#   оргтехники на склад и передачу в определенное подразделение компании. 
#   Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
#   данных, можно использовать любую подходящую структуру, например словарь.

# 6 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
#   пользователем данных. Например, для указания количества принтеров, отправленных 
#   на склад, нельзя использовать строковый тип данных.
# > Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
#              максимум возможностей, изученных на уроках по ООП.

from lesson8.office_tech_classes.OfficeEquipment import AbstractEquipment, Printer, Scanner, MultiFunctionalMacheene as Mfu
from lesson8.office_tech_classes.Warehouse import Warehouse as Store
from lesson8.office_tech_classes.WarehouseException import WarehouseException as StoreEx

def run():
    """Выполняет задания с 4 по 6 к уроку 8"""
    print("\r\nЗадания 4-6\r\n")

    print("Полиморфизм техники: ")
    for item in (Printer(), Scanner(), Mfu()):
        if isinstance(item, AbstractEquipment):
            print(item.description())

    print("\r\nСоздание и заполнение склада")
    warehouse = Store(25)
    list_to_add = {
        Printer(): 4,
        Scanner(): 8,
        Mfu(): 7
        }
    warehouse.add_tech(list_to_add)
    print(warehouse)

    print("\r\nПолучение со склада")
    list_to_delete = {
        Printer(): 2,
        Scanner(): 4,
        Mfu(): 3
        }
    warehouse.get_tech(list_to_delete)
    print(warehouse)

    try:
        print("\r\nПолучение со склада (больше, чем есть)")
        list_to_delete = {
            Printer(): 2,
            Scanner(): 6,
            Mfu(): 3
            }
        warehouse.get_tech(list_to_delete)
    except StoreEx as ex:
        print("Ожидаемая ошибка. " + ex.txt)
    print(warehouse)

    try:
        print("\r\nДобавление на склад (больше, чем может вместить)")
        list_to_add = {
            Printer(): 2,
            Scanner(): 6,
            Mfu(): 30
            }
        warehouse.add_tech(list_to_add)
    except StoreEx as ex:
        print("Ожидаемая ошибка. " + ex.txt)
    print(warehouse)

    try:
        print("\r\nПолучение со склада (строка вместо числа)")
        list_to_delete = {
            Printer(): 2,
            Scanner(): 6,
            Mfu(): 'r'
            }
        warehouse.get_tech(list_to_delete)
    except StoreEx as ex:
        print("Ожидаемая ошибка. " + ex.txt)
    print(warehouse)

    print("\r\nДобавление на склад (норма)")
    list_to_add = {
        Printer(): 4,
        Scanner(): 6,
        Mfu(): 5
        }
    warehouse.add_tech(list_to_add)
    print(warehouse)

    print("\r\nПолучение со склада (норма)")
    list_to_delete = {
        Printer(): 6,
        Scanner(): 10,
        Mfu(): 9
        }
    warehouse.get_tech(list_to_delete)
    print(warehouse)

    print("Задание выполнено\r\n")