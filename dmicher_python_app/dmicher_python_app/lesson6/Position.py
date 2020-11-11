from lesson6.Worker import Worker

class Position(Worker):
    """Класс "Должность" для задания 3"""
    def get_full_name(self):
        """Работник, занимающий позицию"""
        return self.name + " " + self.surname

    def get_total_income(self) -> float:
        """Полная заработная плата на позиции"""
        return sum(self._income_data_.values())
