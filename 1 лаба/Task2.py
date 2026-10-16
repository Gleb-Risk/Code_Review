# FIXME: Множественный комментарий
# Дан файл целых чисел, содержащий более 50 элементов.
# Уменьшить его размер до 50 элементов,
# удалив из файла необходимое количество конечных элементов.
# TODO:
"""
Дан файл целых чисел, содержащий более 50 элементов.
Уменьшить его размер до 50 элементов,
удалив из файла необходимое количество конечных элементов.
"""

import struct
import random
import os

# FIXME: именование функции
# FIXME: Убраны очевидные комментарии
# FIXME: docstring
# TODO:
def binary_file(filename, num_integers):
    """
    Создает двоичный файл с заданным количеством случайных целых чисел.

    :param filename: Имя создаваемого файла
    :param num_integers: Количество целых чисел для записи
    :return None
    """
    with open(filename, 'wb') as f:
        for _ in range(num_integers):
            integer_number = random.randint(-100, 100)
            print(integer_number)
            f.write(struct.pack('i', integer_number)) 


# FIXME: именование функции
# FIXME: Именование константы
# FIXME: docstring
# TODO:
def reduce_binary_file(filename, MAX_SIZE=50):
    """
    Уменьшает размер двоичного файла до заданного количества элементов.

    Удаляет конечные элементы файла, если их количество превышает MAX_SIZE.

    :param filename: Имя файла для обработки
    :param MAX_SIZE: Максимальное количество элементов в файле
    :return None
    """
    with open(filename, 'rb') as f:
        data = f.read()  

    # Определяем количество целых чисел в файле
    count = len(data) // struct.calcsize('i')  

    if count > MAX_SIZE:
        data = data[:MAX_SIZE * struct.calcsize('i')] 

    with open(filename, 'wb') as f:
        f.write(data)  

# Пример использования
file_name = 'integers.bin'
num_integers = int(input('Введите количество целых чисел больше 50 -> '))  

binary_file(file_name, num_integers)

reduce_binary_file(file_name)

# FIXME: длина строки больше 79 символов
# TODO:
with open(file_name, 'rb') as f:
    file_size = os.path.getsize(file_name)
    count = file_size // struct.calcsize('i')
    integers = list(
        struct.unpack('i' * count, f.read())
    )
    print(f'Содержимое двоичного файла после уменьшения:\n{integers}')