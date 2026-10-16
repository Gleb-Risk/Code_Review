"""
Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вставить значение M после каждого третьего элемента списка,
и вывести ссылку на последний элемент полученного списка P2.
"""

#FIXME: Docstring 
#TODO:
class Node:
    def __init__(self, data):
        """
        Конструктор узла списка.

        :param data: Данные, хранящиеся в узле
        :return: None
        """
        self.data = data 1
        self.next = None 


#FIXME: Убраны очевижные комментарии
#FIXME: Наименование переменной
#FIXME: Docstring 
#TODO:
def insert_after_every_third(head, m):
    """
    Вставляет значение m после каждого третьего элемента списка.

    :param head: Указатель на голову списка (P1)
    :param m: Значение для вставки
    :return: Указатель на голову измененного списка
    """
    current = head  
    index = 1  

    while current is not None:
        if index % 3 == 0:
            new_node = Node(m)
            new_node.next = current.next
            current.next = new_node
            current = new_node
        
        current = current.next
        index += 1

    return head  


#FIXME: Docstring 
#TODO:
def get_last_element(head):
    """
    Получает указатель на последний элемент списка.

    :param head: Указатель на голову списка
    :return: Указатель на последний элемент или None, если список пуст
    """
    current = head
    while current.next is not None:
        current = current.next
    return current 


#FIXME: Docstring 
#TODO:
def print_list(head):
    """
    Выводит элементы списка в одну строку.

    :param head: Указатель на голову списка
    :return: None
    """
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")  


if __name__ == "__main__":
    head = None
    current = None

    num_elements = int(input("Введите количество элементов в списке (не менее 3): "))

    if num_elements < 3:
        print("Нужно ввести не менее 3 элементов.")
    else:
        for i in range(num_elements):
            data = int(input(f"Введите значение для элемента {i + 1}: "))
            new_node = Node(data)
            if head is None:
                head = new_node  # Если это первый элемент
                current = head
            else:
                current.next = new_node  # Добавляем новый узел в конец списка
                current = new_node
#FIXME: Наименование переменной
        m = int(input("Введите значение для вставки: "))

        # Вставляем элемент m после каждого третьего элемента
        head = insert_after_every_third(head, )

        print("Полученный список после вставки:")
        print_list(head)

        # Получаем указатель на последний элемент и выводим его данные
        P2 = get_last_element(head)
        print("Значение последнего элемента списка:", P2.data)
