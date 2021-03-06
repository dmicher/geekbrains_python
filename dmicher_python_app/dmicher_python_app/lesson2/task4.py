# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

def run():
    """Выполняет задачу 4 домашнего задания к уроку 2"""
    print("\r\nЗадание 4\r\n")
    user_input = input("Введите несколько слов, разделённых пробелами:\r\n")
    
    if user_input.isspace():
        print("Неверный ввод. Строка не должна быть пустой")
        return

    for part in user_input.split(' '):
        print(part[0:10] if len(part) > 10 else part)

    print("Задание выполнено\r\n")