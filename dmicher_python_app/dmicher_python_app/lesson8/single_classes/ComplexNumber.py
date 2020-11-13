class ComplexNumber():
    """Класс "Комплексные числа" для задания 8"""
    _real: float
    _imag: float

    def __init__(self, real: float = .0, imagine: float = .0):
        """Конструктор принимает 2 необязательных параметра: реальную часть и мнимую"""
        self._real = float(real)
        self._imag = float(imagine)

    def __str__(self):
        """Отображение комплексного числа в записи через выражение (допустима запись в
        виде связной пары [кортежа], но это реже)"""
        return (str(round(self._real, 4)) + " " + str("+ " if self._imag > 0 else "- ") +
                str(abs(round(self._imag, 4))) + "i")

    def __repr__(self):
        """Представление числа дублирует строковое представление"""
        return self.__str__()

    def __add__(self, other: 'ComplexNumber'):
        """Перегрузка операции сложения"""
        return ComplexNumber(
            self._real + other._real,
            self._imag + other._imag
            )

    def __sub__(self, other: 'ComplexNumber'):
        """Перегрузка операции вычетания"""
        return ComplexNumber(
            self._real - other._real,
            self._imag - other._imag
            )

    def __mul__(self, other: 'ComplexNumber'):
        """Перегрузка умножения"""
        return ComplexNumber(
            self._real * other._real - self._imag * other._imag,
            self._real * other._imag + other._real * self._imag
            )

    def __truediv__(self, other: 'ComplexNumber'):
        """Перегрузка операции деления"""
        return ComplexNumber(
            (self._real * other._real + self._imag * other._imag) / (other._real ** 2 + other._imag **2),
            (other._real * self._imag - self._real * other._imag) / (other._real ** 2 + other._imag **2),
            )