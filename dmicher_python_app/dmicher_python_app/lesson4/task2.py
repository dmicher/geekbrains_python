# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента.

# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [1, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]

def run():
    """Выполняет задание 2 для урока № 4"""
    print("\r\nЗадание 2\r\n")
    numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print("Старый список: ", numbers)
    print("Обработанный список: ", [numbers[i] for i in range(len(numbers)) if numbers[i] > numbers[i-1]])
    print("Задание выполнено\r\n")