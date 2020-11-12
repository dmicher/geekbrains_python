# Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
# При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
# Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму 
# этих чисел к полученной ранее сумме и после этого завершить программу.

from tools import Tools as tools

def run():
    """Выполняет задачу _ урока 3"""
    print("\r\nЗаданик 5\r\n")

    is_alive = True  # флаг того, что цикл ввода следует продолжать
    current_sum = .0 # посчитанная текущая сумма

    print("Введите строку чисел, разделённых пробелом. " + 
          "Допустимо ввести несколько строчек.\r\n" +
          "Символы конца ввода: q или й. Числа после конца ввода будут проигнорированы.\r\n" +
          "Прочие нецифровые данные будут проигнорированы без выхода из режима ввода.")

    while is_alive:
        user_input = input("> ")
        user_input = user_input.strip().lower()

        additions = user_input.split()
        for string_value in additions:
            string_value = str(string_value)
            if string_value.count('q') > 0 or string_value.count('й') > 0:
                string_value = string_value[0:min(string_value.find('q'), string_value.find('й'))]
                is_alive = False
            float_value = tools.try_float(string_value)
            current_sum += float_value if float_value is not None else .0
            if not is_alive:
                break

        if is_alive:
            print("Сумма: " + str(current_sum))

    print("Итоговая сумма: " + str(current_sum))
    print("Задание завершено\r\n")
