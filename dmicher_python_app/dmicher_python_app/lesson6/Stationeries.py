class Stationery():
    """Класс "Канцелярская принадлежность" для задания 5"""
    title: str = ''

    def __init__(self, title: str):
        """Инициирует объект, заполняя поле title
        :params title: название канцелярской принадлежности"""
        self.title = title

    def draw(self, content: str):
        """Отрисовка"""
        print(f"\r\nЗапуск отрисовки объекта [{content}]. Отрабатывает " + self.title + ": ")

class Pen(Stationery):
    """Класс "Ручка" для задания 5"""
    def __init__(self):
        return super().__init__(title="ручка")

    def draw(self, content: str):
        """Отрисовка"""
        super().draw(content)
        print("Из-под шариковый ручки выходит сине-белый набросок, на котором изображенa", end=' ')
        print(content)

class Pencil(Stationery):
    """Класс "Карандаш" для задания 5"""
    def __init__(self):
        return super().__init__(title="карандаш")

    def draw(self, content: str):
        """Отрисовка"""
        super().draw(content)
        print("Сначала из-под карандаша, шаркающего по листу, появились робкие очертания, потом " +
              "эти очертания приобрели осмысленность и дерзкую красоту, в результате вышел отличный чертёж, "
              "на котором в трёх декартовых проекциях, с размерами, допусками и посадками красовалась", end=' ')
        print(content)

class Handle(Stationery):
    """Класс "Маркер" для задания 5"""
    def __init__(self):
        return super().__init__(title="маркер")

    def draw(self, content: str):
        """Отрисовка"""
        super().draw(content)
        print("Маркер, как всегда, всё заляпал и извозюкал. Хорошо, что под грязными его линиями всё ещё видна ", end=' ')
        print(content)


