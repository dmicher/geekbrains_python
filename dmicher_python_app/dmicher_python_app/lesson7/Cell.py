from tools import DmicherException

class Cell(object):
    """Класс "клетка" для задания № 3"""
    
    def __init__(self, mesh_count: int):
        """Инициирует объект заданным количество ячеек
        :params mesh_count: количество ячеек, занятых клеткой"""
        if mesh_count < 1:
            raise DmicherException("Невозможно создать клетку: размер меньше чем 1 ячейка.")
        self._mesh_count = mesh_count

    def __add__(self, other):
        """Перегрузка операции сложения"""
        if isinstance(other, Cell):
            return Cell(self._mesh_count + other._mesh_count)
        raise DmicherException("К клетке нельзя прибавлять объекты других классов.")

    def __sub__(self, other):
        """Перегрузка операции вычитания"""
        if isinstance(other, Cell):
            result = self._mesh_count - other._mesh_count
            if result > 0:
                return Cell(result)
            raise DmicherException("Невозможно выполнить вычетание: результат меньше нуля.")
        raise DmicherException("Из клетки нельзя вычитать объекты других классов.")
    
    def __mul__(self, other):
        """Перегрузка операции умножения"""
        if isinstance(other, Cell):
            return Cell(self._mesh_count * other._mesh_count)
        raise DmicherException("Клетку нельзя умножить на объекты других классов.")
    
    def __truediv__(self, other):
        """Перегрузка оператора честного деления"""
        if isinstance(other, Cell):
            result = self._mesh_count // other._mesh_count
            if result < 1:
                raise DmicherException("Невозможно выполнить деление: клетка окажется равной нулю.")
            return Cell(result)
        raise DmicherException("Клетку нельзя умножить на объекты других классов.")

    def make_order(self, row_length: int):
        """Организует ячейки по рядам"""
        if row_length < 1:
            raise DmicherException("Невозможно рассчитать ряды: размер ряда меньше 1.")

        for i in range(self._mesh_count // row_length):
            print("*" * row_length)
        print('*' * (self._mesh_count % row_length))

    def __str__(self):
        """Строковое представление клетки"""
        return "Клетка размером " + str(self._mesh_count) + " яч."

    def __repr__(self):
        """Общее представление клетки"""
        return self.str()