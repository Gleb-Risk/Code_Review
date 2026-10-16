#FIXME: Длина строки > 79 символов, множественный комментарий
#TODO:
"""
ListWork59. 
Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вставить значение M после каждого K-го элемента списка
и вывести ссылку на последний элемент полученного списка P2.
"""

import random


#FIXME: Docstring
#TODO:
class Node:
    def __init__(self, data=None, next=None):
        """
        Конструктор узла.

        :param data: Данные, хранящиеся в узле
        :param next_node: Ссылка на следующий узел
        :return: None
        """
        self.data = data
        self.next = next

    def __str__(self):
        """
        Строковое представление узла.

        :return: Строковое представление данных узла
        """
        return str(self.data)


class LinkedList:
    def __init__(self):
        """
        Конструктор списка.

        :return: None
        """
        self.head = None
        self.tail = None

    def push(self, new_data):
        """
        Добавляет новый элемент в начало списка.

        :param new_data: Данные для нового узла
        :return: None
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

#FIXME: Наименование функции
#TODO:
    def insert_at_begin(self, data):
        """
        Вставляет значение data после каждого k-го элемента списка.

        :param data: Значение для вставки
        :param k: Периодичность вставки (какой по счету элемент)
        :return: None
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

#FIXME: Наименование функции
#TODO:
    def insert_at_index(self, data, index):
        """
        Выводит элементы списка в одну строку.

        :return: None
        """
        new_node = Node(data)
        current_node = self.head
        position = 0

        if index == 0:
            self.insert_at_begin(data)
            return

        while current_node is not None and position + 1 != index:
            position = position + 1
            current_node = current_node.next

        if current_node is not None:
            new_node.next = current_node.next
            current_node.next = new_node
            if new_node.next is None:
                self.tail = new_node

        else:
            print("Index not present")

#FIXME: Наименование функции
#TODO:
    def insert_after_kth(self, data, k):
        current_node = self.head
        count = 0
        while current_node:
            if (count + 1) % k == 0:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                current_node = new_node.next
            else:
                current_node = current_node.next
            count += 1



    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


m = int(input('Введи M: '))
k = int(input('Введи K: '))

lisf = LinkedList()
num_elements = random.randint(5, 20)
for _ in range(num_elements):  # Заполнение списка
    lisf.push(random.randint(1, 45))

current = lisf.head
previous = None
while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
lisf.head = previous

if previous is not None:
    current = lisf.head
    while current.next is not None:
        current = current.next
    lisf.tail = current


print("Исходный список:")
lisf.printLL()
lisf.insert_after_Kth(m, k)

print("Список после вставки:")
lisf.printLL()

if lisf.tail:
    print("Ссылка на последний элемент списка P2:", lisf.tail)
else:
    print("Список пуст.")
