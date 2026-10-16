# FIXME: длина строки > 72, множественный комментарий
#Даны три файла вещественных чисел с именами S1, S2 и S3, элементы которых упорядочены по убыванию.
#Объединить эти файлы в новый файл с именем S4 так, чтобы его элементы также оказались упорядоченными по убыванию.
# TODO:
"""
Даны три файла вещественных чисел с именами S1, S2 и S3,
элементы которых упорядочены по убыванию.
#Объединить эти файлы в новый файл с именем S4 так,
чтобы его элементы также оказались упорядоченными по убыванию.
"""

# FIXME: Убраны очевидные комментарии
# FIXME: docstring
# TODO:
def d_len(iterable):
    """
    Подсчитывает количество элементов в итерируемом объекте.

    :param iterable: Итерируемый объект
    :return: Количество элементов
    """
    elem_count = 0
    for _ in iterable:
        elem_count += 1
    return elem_count


# FIXME: docstring
# TODO:
def sort_files(S1, S2, S3, S4):
    """
    Объединяет три файла с числами в один, сохраняя порядок по убыванию.

    :param s1: Имя первого входного файла
    :param s2: Имя второго входного файла
    :param s3: Имя третьего входного файла
    :param s4: Имя выходного файла
    :return None
    """
    numbers = []


# FIXME: docstring
# TODO:
    def read_file(filename):
        """
        Читает вещественные числа из файла, по одному в строке.

        :param filename: Имя файла для чтения   
        :return: Список вещественных чисел
        """
        with open(filename, 'r') as f:
            return [float(line.strip()) for line in f.readlines()] 

    numbers.extend(read_file(S1))
    numbers.extend(read_file(S2))
    numbers.extend(read_file(S3))

# FIXME: docstring
# TODO:
    def sort_numbers(arr):
        """
        Сортирует список вещественных чисел по убыванию.

        Использует алгоритм сортировки вставками (insertion sort).

        :param arr: Список чисел для сортировки
        :return: Отсортированный список (по убыванию)
        """
        for i in range(1, d_len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    numbers = sort_numbers(numbers)

    with open("S4.txt", 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

    print(f"Файлы {S1}, {S2}, и {S3} объединены в {S4}.")

sort_files('S1', 'S2', 'S3', 'S4')
