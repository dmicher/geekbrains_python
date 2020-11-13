from lesson8.office_tech_classes.WarehouseException import WarehouseException
from lesson8.office_tech_classes.OfficeEquipment import AbstractEquipment
import os
from datetime import datetime
from tools import Tools as tools

class Warehouse(object):
    """Класс "Склад" офисной техники"""
    _total_place: int
    _tech_placed: dict
    __log_path: str

    def __init__(self, total_place: int = 0):
        """Инициирует склад, определяя его объём и создавая пустой объём хранения"""
        self._total_place = total_place
        self._tech_placed = {}
        self.__log_path = os.path.join(tools.get_dir(), "lesson8_warehouse.log")

    def add_tech(self, equipment_to_place: dict):
        """Добавляет технику на склад по словарю"""
        self._validate_dict(equipment_to_place)

        if self.free_place < sum(equipment_to_place.values()):
            mes = ("Склад не может вместить указанное количество техники. Свободно: " + 
                   str(self.free_place) + ", требуется: " + str(sum(equipment_to_place.values())))
            self._log_event(mes)
            raise WarehouseException(mes)

        for eq_names, eq_values in ((str(AbstractEquipment(x).name), y) for x, y in equipment_to_place.items()):
            if eq_names in self._tech_placed:
                self._tech_placed[eq_names] += eq_values
            else:
                self._tech_placed[eq_names] = eq_values
        self._log_event("Успешное добавление на склад\r\n" + str(equipment_to_place))

    def get_tech(self, equipment_to_get: dict):
        """Выдаёт технику со склада по словарю"""
        self._validate_dict(equipment_to_get)

        # не произвожу вычитание сразу, т.к. обеспечиваю транзакционность: проведётся либо всё, либо ничего
        to_give_dict = {(str(AbstractEquipment(x).name), y) for x, y in equipment_to_get.items()}
        for eq_name, eq_value in to_give_dict:
            if eq_name in self._tech_placed.keys():
                if self._tech_placed[eq_name] < eq_value:
                    mes = ("Склад не может выдать требуемую технику. " +
                           "На складе недостаточно " + eq_name + ". Требуется " +
                           str(eq_value) + ", в наличии " + str(self._tech_placed[eq_name]))
                    self._log_event(mes)
                    raise WarehouseException(mes)
            else:
                mes = ("Склад не может выдать требуемую технику. На складе отсутствует " + eq_name)
                self._log_event(mes)
                raise WarehouseException(mes)

        for eq_name, eq_value in to_give_dict:
            self._tech_placed[eq_name] -= eq_value
        self._log_event("Успешное получение со склада" + str(equipment_to_get))

    def __str__(self):
        """Вывод информации по складу"""
        return (f"Склад. Мест всего: {self._total_place}, сводобно {self.free_place} \r\nСодержание: " 
                + str(self._tech_placed))

    def __repr__(self):
        """Вывод информации по складу (для вложенных классов)"""
        return self.__str__()

    def _validate_dict(self, equipnet_dict: dict):
        """Проверяет приемлемость словаря для работы с текущим объектом"""
        if equipnet_dict == None or len(equipnet_dict) == 0:
            mes = "На склад передан пустой словарь."
            self._log_event(mes)
            raise WarehouseException(mes)

        for key in equipnet_dict.keys():
            if not isinstance(key, AbstractEquipment) or type(equipnet_dict[key]) != int or int(equipnet_dict[key]) < 0:
                mes = ("На склад передан словарь с неприемлемым форматом данных. " +
                                         "Проверьте типы данных и количество передаваемой техники")
                self._log_event(mes)
                raise WarehouseException(mes)

    @property
    def free_place(self):
        """Остаток свободного места на складе"""
        return self._total_place - sum(x for x in self._tech_placed.values())

    def _log_event(self, message: str):
        try:
            with open(self.__log_path, 'a+') as stream:
                stream.write(str(datetime.now()) + " " + message + "\r\n")
        except Exception as ex:
            raise WarehouseException("Провал ведения логов." + str(ex))