from tools import DmicherException

class Matrix():
    """Класс "Матрица" для задания № 1"""
    def __init__(self, content: [[int]]):
        """Инициализация матрицы с содержимым"""
        if len(content) < 1 or len(content[0]) < 1:
            raise DmicherException("Невозможно создать матрицу нулевого размера")
        
        self._rows_count = len(content)
        self._columns_count = len(content[0])
        
        for row in content:
            if self._columns_count != len(row):
                raise DmicherException("Создание непрямоугольной матрицы не допустимо в этом объекте. " +
                                       "Убедитесь, что все строки имеют одинаковую длину.")

        self._content = content

    def __str__(self):
        """Выводит строковое представление матрицы"""
        string = "Матрица размерами: " + str(self._rows_count) + "/" + str(self._columns_count)

        for row in self._content:
            string += "\r\n"
            for cell in row:
                string += str(cell) + " "

        return string

    def __add__(self, other):
        """Складывает две матрицы"""
        if type(other) is not Matrix:
            raise DmicherException("Невозможно сложить матрицу с объектом, не являющимся матрицей")

        if self._rows_count != other._rows_count or self._columns_count != other._columns_count:
            raise DmicherException("Невозможно сложить матрицы. Они имеют разный размер.")

        new_content = []
        for i in range(self._rows_count):
            row = []
            for j in range(self._columns_count):
                row.append(self._content[i][j] + other._content[i][j])
            new_content.append(row)

        return Matrix(new_content)

    def __mul__(self, num: int):
        """Умножает матрицу на число"""
        new_content = []
        for i in range(self._rows_count):
            row = []
            for j in range(self._columns_count):
                row.append(self._content[i][j] * num)
            new_content.append(row)

        return Matrix(new_content)

    def __sub__(self, other):
        """Вычитает из одной матрицы другую"""
        return self + (other * -1)
