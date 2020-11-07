# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы 
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#       Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#       Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#       Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#       Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

def run():
    """Выполняет задачу 5 домашнего задания к уроку 2"""
    print("\r\nЗадание 5\r\n")

    sequence = []

    while True:
        print("Текущая структура данных:", sequence)
        user_input = input("Введите следующий элемент (нечисловое значение - выход): ")

        if not user_input.isdigit():
            print("Ввод данных прекращён.")
            break

        value = int(user_input)

        # Отбросим простейшие варианты (это позволит упростить дальнейший алгоритм)
        # пока нет никаких значений или новое число меньше или равно меньшему из массива - вставить новое значение в хвост
        if len(sequence) == 0 or value <= sequence[len(sequence) - 1]:
            sequence.append(value)
            continue
        # новое значение больше большего из массива - вставить в начало (если равно, то по задаче - вставлять правее)
        if value > sequence[0]:
            sequence.insert(0, value)
            continue
        # не меньше меньшего, не больше большего, но между крайними значениями пока никого нет - вставить посредине
        if len(sequence) == 2:
            sequence.insert(1, value)
            continue

        # Если попал сюда, то новое значение надо вставить куда-то внутрь массива: надо понять, куда.
        # Для малых массивов приемлем прямой перебор значений, но для больших массивов это неоптимально.
        # Поскольку наш список всегда сортирован, можно реализовать метод дихотомии для поиска.

        direction = 1                   # направление следующего шага, может быть "1" и "-1"
        current_index = 0               # текущее положение бегунка
        step_size = len(sequence) // 2  # размер следующего шага

        while True:
            # Делает очередной шаг. Пока это имеет смысл, сокращает размер шага вдвое для следующей итерации
            current_index += direction * step_size
            step_size = step_size // 2 if step_size > 2 else 1

            # Смотрит, куда пришёл: если пришёл в место, куда надо вставить значение, делает и выходит. 
            # Иначе - ищет новое направление, куда шагнуть, и переходит к следующей итерации.
            if value == sequence[current_index]: # попал в число, равное вставляемому - искать правее
                direction = 1
            elif value > sequence[current_index]: # попал в меньшее число
                if value <= sequence[current_index - 1]: # а слева - не меньше, чем вставляемое: нашёл, куда ставить
                    sequence.insert(current_index, value)
                    break
                direction = -1 # а слева число толе меньшее чем вставляемое: искать левее
            else: # попал в большее число: ситуация, обратная предыдущей
                if value >= sequence[current_index]:
                    sequence.insert(current_index + 1, value)
                    break
                direction = 1

    print("Задание выполнено\r\n")