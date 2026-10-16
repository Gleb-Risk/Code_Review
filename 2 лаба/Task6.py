#FIXME: Длина строки > 79
#TODO:
"""
Dynamic78. 
Даны ссылки A1 и A2 на барьерный и текущий элементы двусвязного списка.                              
Включить в класс IntListB процедуры ToFirst 
(делает текущим первый элемент списка),
ToNext (делает текущим следующий элемент в списке), SetData(D) 
(присваивает текущему элементу списка
значение D целого типа, если данный элемент не является барьерным) и
функцию IsBarrier логического типа (возвращает true, если текущий
элемент списка является его барьерным элементом, и false в противном случае). 
Методы ToFirst, ToNext и IsBarrier не имеют параметров. 
Параметр D метода SetData является входным параметром целого типа. 
С помощью этих методов присвоить нулевые значения элементам
исходного списка с нечетными номерами и вывести количество элементов в списке,
а также ссылку на новый текущий элемент списка 
(текущим элементом списка должен стать его барьерный элемент). 
Нумерация ведется от первого элемента списка; барьерный элемент не
нумеруется и не учитывается при подсчете элементов.
Описать класс IntListB, содержащий следующие члены:
• закрытые поля barrier и current типа Node 
(барьерный и текущий элементы списка);
• конструктор с параметрами aBarrier и aCurrent — 
барьерным и текущим элементами существующего списка;
• процедура InsertLast(D), 
которая добавляет новый элемент со значением D в конец списка
(D — входной параметр целого типа, добавленный элемент становится текущим);
• процедура Put (без параметров), которая выводит ссылку на поле current,
используя метод Put класса PT.
С помощью метода InsertLast добавить в конец исходного списка данный набор чисел 
(в том же порядке) и вывести сссылку на текущий элемент полученного списка,
используя для этого метод Put класса IntListB.
"""
# import gc

#FIXME: Docstring
#FIXME: Наименование функции
#TODO:
def node_to_str(x): 
    """
    Возвращает строковое представление адреса узла.

    :param node: Узел списка
    :return: Строка с адресом или None
    """
    if x is None: return None
    else: return str(x)[-5:-1]

class Node:
    def __init__(self, data = None, next = None, prev = None):
        """
        Конструктор узла.

        :param data: Данные узла
        :param next_node: Ссылка на следующий узел
        :param prev_node: Ссылка на предыдущий узел
        :return: None
        """
        self.data = data
        self.next = next
        self.prev = prev


class IntListB:
    __initNode = Node()
    __barrier = __initNode
    __current = __initNode

    def __init__(self):
        """
        Конструктор списка.

        :param barrier: Барьерный элемент
        :param current: Текущий элемент
        :return: None
        """
        self.aBarrier = self.__barrier
        self.aCurrent = self.__current
        self.aBarrier.next = self.aBarrier
        self.aBarrier.prev = self.aBarrier

#FIXME: Наименование переменной
    def insert_last(self, d):
        """
        Добавляет новый элемент со значением data в конец списка.

        :param data: Данные для нового узла
        :return: None
        """
        newNode = Node(d, self.aBarrier, self.aBarrier.prev)
        self.aCurrent = newNode
        self.aBarrier.prev.next = newNode
        self.aBarrier.prev = newNode

    def to_first(self):
        """
        Делает текущим первый элемент списка.

        :return: None
        """
        self.aCurrent = self.aBarrier.next
    
    def to_next(self):
        """
        Делает текущим следующий элемент в списке.

        :return: None
        """
        self.aCurrent = self.aCurrent.next

    def set_data(self, d):
        """
        Присваивает текущему элементу значение data, если он не барьерный.

        :param data: Новое значение
        :return: None
        """
        if self.IsBarrier():
            pass
        else:
            self.aCurrent.data = d

    def is_barrier(self):
        """
        Проверяет, является ли текущий элемент барьерным.

        :return: True, если текущий элемент барьерный, иначе False
        """
        if self.aCurrent is self.aBarrier:
            return True
        else:
            return False

#FIXME: Убраны не нужные комментарии
#TODO:

    def put(self):
        """
        Выводит ссылку на поле current, используя метод put класса PT.

        :return: None
        """
        node = PT().Put(self.aCurrent)
        print('Адрес поля current:', node)

#FIXME: Убран не нужный многострочный комментарий
#TODO:


class PT():
    def Put(self, cur):
        return cur
    

il = IntListB()
for i in range(7):
    il.insert_last(i)

print('Адрес барьерного элемента:', il.aBarrier)
il.Put()
print()

il.to_first()
i = 0
while not(il.is_barrier()):
    i += 1
    if (i % 2) != 0:
        il.set_data(None)
    print('Узел', i, end=') '); il.Put()
    print('его значение:',il.aCurrent.data)
    il.to_next()

print('\nВсего элементов:', i)
il.Put()