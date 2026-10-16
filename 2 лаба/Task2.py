#FIXME: Длина строки > 79 
#TODO:
"""
Дано число n (> 0) и две непустые очереди; начало и конец первой равны A1 и A2,
а второй — A3 и A4.
Переместить n начальных элементов первой очереди в конец второй очереди.
Если первая очередь содержит менее n элементов, то переместить из первой очереди
во вторую все элементы. 
Вывести новые ссылки на начало и конец первой, а затем второй
очереди (для пустой очереди дважды вывести null). 
Новые объекты типа Node не создавать.
"""

#FIXME: Убраны очевидные комментарии
#FIXME: Docstring
#TODO:
class Node:  # Узел очереди
    def __init__(self, data): 
        """
        Конструктор узла очереди.

        :param data: Данные, хранящиеся в узле
        :return: None
        """ 
        self.data = data  
        self.next = None  

class Queue:  
    def __init__(self):
        """
        Конструктор очереди.

        :return: None
        """  
        self.head = None  
        self.end = None  

    def enqueue(self, data):  
        """
        Добавляет элемент в конец очереди.

        :param data: Данные для добавления
        :return: None
        """
        new_node = Node(data) 
        if self.head is None:  
            self.head = new_node  
            self.end = new_node
        else:  
            self.end.next = new_node  
            self.end = new_node 

    def dequeue(self):  
        """
        Удаляет и возвращает элемент из начала очереди.

        :return: Данные из начала очереди или None, если очередь пуста
        """
        if self.head is None:  
            return None 
        data = self.head.data  
        self.head = self.head.next 
        if self.head is None:  
            self.end = None  
        return data  

    def print_queue(self):  
        """
        Выводит элементы очереди в одну строку.

        :return: None
        """
        current = self.head  
        if not current: 
            print("Очередь пуста", end=" ")
        while current:  
            print(current.data, end=" ") 
            current = current.next  
        print()  

def move_queue(q1, q2, n): 
    """
    Перемещает n элементов из первой очереди в конец второй.

    Новые объекты типа Node не создаются, узлы переносятся целиком.
    Если в первой очереди меньше n элементов, переносятся все.

    :param q1: Первая очередь (источник)
    :param q2: Вторая очередь (приемник)
    :param n: Количество элементов для перемещения
    :return: Кортеж из новых ссылок (head1, end1, head2, end2)
    """
    if q1.head is None:  
        return q2.head, q2.end  

    
    count = 0
    while count < n and q1.head is not None:  
        data = q1.dequeue()  
        q2.enqueue(data)  
        count += 1

    return q1.head, q1.end, q2.head, q2.end

#FIXME: наименование переменной
# Ввод числа n с проверкой > 0
while True:
    try:
        n = int(input("Введите число n (> 0): "))
        if n > 0:
            break
        else:
            print("Ошибка: n должно быть больше 0. Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целое положительное число.")

#FIXME: Длина строки > 79 символов, перенос внутри скобок
#TODO:
queue1 = Queue()  
while True:
    try:
        num_elements1 = int(
            input("Введите количество элементов в 1 очереди: ")
        )
        if num_elements1 > 0:
            break
        print("Ошибка: количество элементов должно быть больше 0.")
    except ValueError:
        print("Ошибка: введите целое положительное число.")


#FIXME: Длина строки > 79 символов, перенос внутри скобок
#TODO:
elements1 = input(
    "Введите элементы для 1 очереди, разделенных пробелами: "
).split()

#FIXME: Длина строки > 79 символов, перенос внутри скобок
#TODO:
while len(elements1) != num_elements1:
    print(
        f"Ошибка: количество введенных элементов должно быть "
        f"равно {num_elements1}. Попробуйте снова."
    )
    elements_1 = input(
        "Введите элементы для 1 очереди, разделенных пробелами: "
    ).split()

for elem in elements1:  
    queue1.enqueue(elem)

#FIXME: Длина строки > 79 символов, перенос внутри скобок
#TODO:
queue2 = Queue()
while True:
    try:
        num_elements2 = int(
            input("Введите количество элементов во 2 очереди: ")
        )
        if num_elements2 > 0:
            break
        print("Ошибка: количество элементов должно быть больше 0.")
    except ValueError:
        print("Ошибка: введите целое положительное число.")

#FIXME: Длина строки > 79 символов, перенос внутри скобок
#TODO:
elements2 = input(
    "Введите элементы для 2 очереди, разделенных пробелами: "
).split()

while len(elements2) != num_elements2:
    print(
        f"Ошибка: количество введенных элементов должно быть "
        f"равно {num_elements2}. Попробуйте снова."
    )
    elements_2 = input(
        "Введите элементы для 2 очереди, разделенных пробелами: "
    ).split()

for elem in elements2:  
    queue2.enqueue(elem)

print("\nОчередь 1:")  
queue1.print_queue()
print("Очередь 2:")  
queue2.print_queue()

# Перемещение n элементов из queue1 в queue2
head1, end1, head2, end2 = move_queue(queue1, queue2, n)  

print("\nПосле перемещения:")
print("Очередь 1:")  
queue1.print_queue()
print("Очередь 2:")  
queue2.print_queue()

# Вывод новых ссылок на начало и конец очередей
print(f"\nНачало очереди 1: {queue1.head if queue1.head else 'null'}")  
print(f"Конец очереди 1: {queue1.end if queue1.end else 'null'}")  
print(f"\nНачало очереди 2: {queue2.head if queue2.head else 'null'}")  
print(f"Конец очереди 2: {queue2.end if queue2.end else 'null'}")  