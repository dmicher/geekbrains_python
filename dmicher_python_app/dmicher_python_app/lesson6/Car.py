class Car():
    """Объект "Машина" для задания 4"""
    _speed_: float
    _color_: str
    _name_: str
    _is_police_: bool
    _base_speed_: float
    _max_accelerations_count_: int

    def __init__(self, base_speed: float, max_accelerations: int, name: str, color: str, is_police: bool = False):
        """Инициирует поведение машины
        :params base_speed: базовая скорость машины (шаг в ускорении и замедлении)
        :params max_accelerations: максимальная скорость (количево шагоу ускорения)
        :params name: название типа автомобиля
        :params color: цвет автомобиля
        :params is_police: является ли автомобиль полицейским"""
        self._speed_ = 0
        self._color_ = color
        self._name_ = name
        self._is_police_ = is_police
        self._base_speed_ = base_speed
        self._max_accelerations_count_ = max_accelerations
        
    def __str__(self):
        """Преобразует объект в строку"""
        return self._color_ + " " + self._name_

    def go(self):
        """Команда машине двигаться"""
        if not self._speed_:
            self._speed_ = self._base_speed_
            print(str(self) + " начал движение и движется со скоростью " + str(self._speed_))
        else:
            print(str(self) + " продолжает движение со скоростью " + str(self._speed_))

    def speed_up(self):
        """Команда машине увеличить свою скорость"""
        if self._speed_ == 0:
            self.go()
        elif self._speed_ >= self._max_accelerations_count_ * self._base_speed_:
            if self._speed_ > self._max_accelerations_count_ * self._base_speed_:
                self._speed_ = self._max_accelerations_count_ * self._base_speed_
            print(str(self) + " едет на своей предельной скорости " + str(self._speed_) + 
                  ". Ускорение невозможно.")
        else:
            self._speed_ += self._base_speed_
            print(str(self) + " ускорился и теперь едет со скоростью " + str(self._speed_))

    def slow_down(self):
        """Команда машине снизить свою скорость"""
        if self._speed_ <= self._base_speed_:
            self.stop()
        else:
            self._speed_ -= self._base_speed_
            print(str(self) + " замедлился до скорости " + str(self._speed_))

    def stop(self):
        """Команда машине остановиться"""
        if self._speed_:
            print(str(self) + " остановился.")
            self._speed_ = .0
        print(str(self) + " продолжает стоять.")

    def show_speed(self) -> float:
        """Показывает текущую скорость автомобиля"""
        return "Машина едет со скоростью " + str(self._speed_)

    def wait(self):
        """Команде машине продолжать, что делала """
        if self._speed_ == 0:
            self.stop();
        else:
            self.go()

    def direction(self, direction: str):
        """Команда машине совершить поворот
        Машина не может поворачивать, пока стоит.
        :param direction: направление поворота: r-направо, l-налево, o-разворот."""
        if self._speed_ == 0:
            pritn(str(self) + " не может поворачивать, пока стоит.")
            return

        if direction == "r":
            print(str(self) + " поворачивает направо.")
        elif direction == "l":
            print(str(self) + " поворачивает налево.")
        elif direction == "o":
            print(str(self) + " разворачивается.")
        else:
            print(f"Недопустимый манёвр. {str(self)} продолжает движение.")


