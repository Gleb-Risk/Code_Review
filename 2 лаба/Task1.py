# FIXME: Длина строки больше 72 символов, множественный комментарий
# Вариант 7 Dynamic9 Dynamic18 ListWork7 ListWork24 ListWork61
# Даны вершины A1 и A2 двух непустых стеков. 
# Перемещать элементы из первого стека во второй, пока значение вершины первого стека не станет четным (перемещенные элементы первого стека будут располагаться во втором стеке в порядке, обратном исходному). 
# Если в первом стеке нет элементов с четными значениями, то переместить из первого стека во второй все элементы. 
# Вывести ссылки на новые вершины первого и второго стека (если первый стек окажется пустым, то вывести для него константу null). 
# Новые объекты типа Node не создавать.
# TODO: 
"""
Вариант 7 Dynamic9 Dynamic18 ListWork7 ListWork24 ListWork61
Даны вершины A1 и A2 двух непустых стеков. 
Перемещать элементы из первого стека во второй,
пока значение вершины первого стека не станет четным
(перемещенные элементы первого стека будут 
располагаться во втором стеке в порядке, обратном исходному). 
Если в первом стеке нет элементов с четными значениями,
то переместить из первого стека во второй все элементы. 
Вывести ссылки на новые вершины первого и второго стека
(если первый стек окажется пустым, то вывести для него константу null). 
Новые объекты типа Node не создавать.
"""
import random

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item): # Добавление элемента
        self.data.append(item)

    def pop(self):
        if self.is_emtpy(): # Удаление элемента
            raise IndexError("Стек пустой")
        return self.data.pop()
    
    def peek(self): # Просмотр первой вершины
        if self.is_emtpy(): 
            raise IndexError("Стек пустой")
        return self.data[-1]
    
    def is_emtpy(self): # Пустота стека
        return len(self.data) == 0
    
    def __str__(self): # Вывод всего стека
        return str(self.data)

# FIXME: именование переменных
# TODO:
def main():   
    stack_a1 = Stack()
    stack_a2 = Stack()
    # заполнение стеков
    for _ in range(2, 20):
        num = random.randint(0, 100)
# FIXME: Убраны неактуальные комментарии
# TODO:
        stack_a1.push(num)
    
    for _ in range(1, 5):
        num = random.randint(0, 100)
        stack_a2.push(num)
    # Вывод стеков
    print(f"стек 1-> {stack_a1.__str__()}\nВершина->{stack_a1.peek()}")
    print(f"стек 2-> {stack_a2.__str__()}\nВершина->{stack_a2.peek()}")
# FIXME: Убран очевидный комментарий
# TODO: 
    while not stack_a1.is_emtpy() and stack_a1.peek() % 2 != 0: 
        stack_a2.push(stack_a1.pop())
# FIXME: длинаа строки больше 79 символов
# TODO:        
    if not stack_a1.is_empty():
        print(
            f"Новая вершина 1 ст->{stack_a1.peek()}\n"
            f"Ссылка вершины 1 ст->{id(stack_a1.peek())}"
        )
    else:
        print("null")

    print(
        f"Новая вершина 2 ст->{stack_a2.peek()}\n"
        f"Ссылка вершины 2 ст->{id(stack_a2.peek())}"
    )

if __name__ == "__main__":
    main()