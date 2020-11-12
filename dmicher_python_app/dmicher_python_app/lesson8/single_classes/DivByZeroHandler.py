class ZeroDivisionHandler:
    """Класс, содержащий обработчик исключений деления на ноль"""
    
    @staticmethod
    def handle_decorator(func):
        """Декоратор, обрабатывающий исключения при делении на ноль"""
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except ZeroDivisionError as exc:
                print("Зафиксирована попытка разделить на ноль. Фу таким быть!")

        return wrapper