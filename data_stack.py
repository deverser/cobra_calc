class DataStack():
    """Класс для сохранения операндов калькулятора"""
    def __init__(self):
        # Создаем стек в виде списка stack
        self.stack = []

    def isEmpty(self):
        """Проверка на отсутствие данных в стеке"""
        return len(self.stack) == 0

    def push(self, item):
        """Добавление данных в стек"""
        self.stack.append(item)

    def pop(self):
        """Извлечение данных из стека"""
        return self.stack.pop()

    def peek(self):
        """Извлечение первого элемента"""
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.stack[len(self.stack)-1]

    def size(self):
        """Размер стека"""
        return len(self.stack)

    def show(self):
        """Отображение стека"""
        return self.stack
