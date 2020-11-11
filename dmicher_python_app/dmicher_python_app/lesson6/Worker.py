class Worker(object):
    """Класс "Работник" для задачи 3"""
    name: str
    surname: str
    position: str
    _income_data_ = {"wage": .0, "bonus": .0}
    _income_: float = _income_data_["wage"]

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        """Инициирует новый объект работника. Все поля обязательны"""
        self.name = name
        self.surname = surname
        self.position = position
        self._income_data_ = {"wage": wage, "bonus": bonus}

