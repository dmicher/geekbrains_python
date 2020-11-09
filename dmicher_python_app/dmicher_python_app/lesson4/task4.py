# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. 
# Элементы вывести в порядке их следования в исходном списке. 
# Для выполнения задания обязательно использовать генератор.

# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import time

def run():
    """Выполняет задание 4 для урока № 4"""
    print("\r\nЗадание 4\r\n")

    numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    print("\r\n=======================================================================================================")
    print("------------------------ ПРОСТОЙ ВАРИАНТ (небольшой массив, есть повторения) -------------------------")
    print("-------------------------------оба алгоритма должны отработать быстро---------------------------------")
    print("Исходный массив 1: ", numbers)
    advantage(algorythm1(numbers, True), algorythm2(numbers, True))
    print("\r\n=======================================================================================================")
    print("---------------------- АСИМПТОТИЧЕСКИЙ ВАРИАНТ (огромный массив, нет повторений) ----------------------")
    print("-----------------------------выполняется долго, преимущество у алгоритма 2-----------------------------")
    numbers = list(range(0, 50_000))
    print("Наберитесь терпения (до пары минут в зависимости от машины) - выполняется...")
    advantage(algorythm1(numbers), algorythm2(numbers))
    print("\r\n=======================================================================================================")
    print("------------------------ СМЕШАННЫЙ ВАРИАНТ (большой массив, много повторений) -------------------------")
    print("-----------------------------выполняется долго, преимущество у алгоритма 2-----------------------------")
    numbers = list(range(0, 5_000))
    numbers.extend(list(range(0, 1500, 2)))
    numbers.extend(list(range(0, 1500, 3)))
    numbers.extend(list(range(0, 1500, 4)))
    advantage(algorythm1(numbers), algorythm2(numbers))
    print("Задание выполнено\r\n")

def algorythm1(numbers, dispay_array=False):
    """Алгоритм 1: написание в одну строчку
    Асимптотическая сложность: О(N^2). Достигается при бесконечном массиве вне зависимости от повторений.
    Время выполнения растёт по квадрату от размера исходного массива:
    для каждого из элемента массива происходит пробег по всем элементам массива (N*N), чтобы посчитать их количество.
    Введём проверку по времени выполнения и сравним с алгоритмом 2
    
    :param numbers: перечисление произвольных целых чисел -> [int]
    """
    print("\r\nАлгоритм 1.")
    start = time.time()
    result = [item for item in numbers if numbers.count(item) < 2]
    if dispay_array:
        print("Обработанный массив: ", result)
    else:
        print("Объём исходного массива: ", len(numbers), "Объём итогового массива: ", len(result))
    return round(time.time() - start, 6)

def algorythm2(numbers, dispay_array=False):
    """Алгоритм 2 (сложнее в написании, но будет работать быстрее на больших массивах при множественном повторении)
    Асимптотическая сложность: O(N). Достигается при бесконеном массиве с отсутствием повторений.
    Время выполнения растёт по квадрату от размера исходного массива:
    - 1 пробег O(N) для составления частотного массива; 
    - многократные обращения к словарю для получения и записи: O(1) для каждого отдельного обращения; в асимптоте - O(3*N);
    - 1 пробег O(N) по всем элементам основного массива;

    :param numbers: перечисление произвольных целых чисел -> [int]
    """
    print("\r\nАлгоритм 2.")
    start = time.time()
    frequency_dict = {}
    # получение и присваивание - по O(1), всего O(N) [при всех уникальных в numbers]
    for num in numbers:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    result = [item for item in (key for key, value in frequency_dict.items() if value < 2)]
    # дополнительно О(N) [при всех уникальных в numbers] - по одному пробегу за каждый цикл
    if dispay_array:
        print("Обработанный массив: ", result)
    else:
        print("Объём исходного массива: ", len(numbers), "Объём итогового массива: ", len(result))
    return round(time.time() - start, 6)

def advantage(alg1_time: float, alg2_time: float):
    """Рассчитывает и выводит на экран преимущество между алгоритмами
    
    :param alg1_time: время выполнения алгоритма № 1 в секундах -> float
    :param alg2_time: время выполнения алгоритма № 2 в секундах -> float
    """
    print("\r\nИТОГО:")
    if alg1_time == 0:
        if alg2_time == 0:
            print("Преимущество не обнаружено. Оба алгоритма выполнились моментально.")
            return
        else:
            print("Алгоритм 1 выполнен моментально. Алгоритм 2 за " + str(alg2_time) + " сек.")
            return
    elif alg2_time == 0:
        print("Алгоритм 2 выполнен моментально. Алгоритм 1 за " + str(alg1_time) + " сек.")
        return

    if alg1_time == alg2_time:
        print("Преимущество не обнаружено. Оба алгоритма выполнились за " + str(alg1_time) + " сек.")
        return

    print("Время выполнения алгоритмов:")
    print("- алгоритм 1 = " + str(alg1_time) + " сек.")
    print("- алгоритм 2 = " + str(alg2_time) + " сек.")
    if alg1_time > alg2_time:
        print("Алгоритм 2 выполнился быстрее алгоритма 1 в " + str(round(alg1_time/alg2_time)) + " раз(а)." )
    else:
        print("Алгоритм 1 выполнился быстрее алгоритма 2 в " + str(round(alg2_time/alg1_time)) + " раз(а)." )