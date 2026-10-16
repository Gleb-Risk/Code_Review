#FIXME: Длина строки > 79 символов
#TODO:
""" 
Даны ссылки A1 и A2 на первый и последний элементы непустого двусвязного
списка,
содержащего четное количество элементов. Преобразовать список в
два циклических списка 
( записав в свойство Next последнего элемента списка ссылку на его первый
элемент, а в свойство Prev первого элемента — ссылку на последний элемент.),
первый из которых содержит первую
половину элементов исходного списка, а второй — вторую половину. Вывести
ссылки A3 и A4 на два средних элемента исходного списка
(элемент A3 должен входить в
первый циклический список, а элемент A4 — во второй). 
Новые объекты типа Node не создавать.
"""


#FIXME: Убраны очевидные комментарии
#FIXME: Docstring
#TODO:
class Node:
    """Класс, представляющий узел двусвязного списка."""

    def __init__(self, data):
        """
        Конструктор узла.

        :param data: Данные, хранящиеся в узле
        :return: None
        """
        self.data = data  
        self.prev = None  
        self.next = None  


class DoublyLinkedList:
    """Класс, реализующий двусвязный список."""

    def __init__(self):
        """
        Конструктор списка.

        :return: None
        """
        self.first = None 
        self.last = None  
        self.current = None  

    def append(self, data):
        """
        Добавляет новый узел в конец списка.

        :param data: Данные для добавления
        :return: Созданный узел
        """
        new_node = Node(data)
        if not self.first:  
            self.first = self.last = new_node
        else:
            self.last.next = new_node  
            new_node.prev = self.last  
            self.last = new_node  
        return new_node

    def split_into_circular(self):
        """"
        Разбивает список на два циклических списка.

        :return: Кортеж (начало1, конец1, начало2, конец2, средний1, средний2)
        """
        if not self.first or not self.first.next:
            return None, None, None, None

        slow = self.first
        fast = self.first

        # Найдем середину списка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Определяем две половины списка
        mid1 = slow.prev  
        mid2 = slow  

        # Создаем первый циклический список
        first_half_first = self.first
        first_half_last = mid1
        first_half_last.next = first_half_first  
        first_half_first.prev = first_half_last

        # Создаем второй циклический список
        second_half_first = mid2
        second_half_last = self.last
        second_half_last.next = second_half_first  
        second_half_first.prev = second_half_last

#FIXME: Длина строки > 79 
#TODO:
        return (
            first_half_first, first_half_last,
            second_half_first, second_half_last,
            mid1, mid2
        )

    def display(self, start_node):
        """
        Выводит циклический список на экран.

        :param start_node: Узел, с которого начинается вывод
        :return: None
        """
        if not start_node:
            print("Список пуст")
            return
        current = start_node
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == start_node:
                break
        print("(circular)")


# Пользовательский интерфейс
if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    # Ввод данных
    n = int(input("Введите четное количество элементов списка: "))
    for i in range(n):
        data = input(f"Введите элемент {i + 1}: ")
        linked_list.append(data)

#FIXME: Длина строки > 79 
#TODO:
    # Разделение на два циклических списка
    (
        first_half_first, first_half_last,
        second_half_first, second_half_last,
        A3, A4
    ) = linked_list.split_into_circular()

    # Вывод результатов
    print("\nПервый циклический список:")
    linked_list.display(first_half_first)
    print("\nВторой циклический список:")
    linked_list.display(second_half_first)

    print("\nСредний элемент первого списка (A3):", A3.data if A3 else None)
    print("Средний элемент второго списка (A4):", A4.data if A4 else None)