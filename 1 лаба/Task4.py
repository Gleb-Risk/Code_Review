# FIXME:длина строки больше 72 символов, множественный комментарий:
#Имеется информация об учениках начальной школы. Для всех учеников известны:
#фамилия, имя и класс. Для учеников 1-х классов дополнительно известна их скорость чтения
#(слов в минуту, тип int). Для учеников 4-х классов известны баллы итоговой аттестации (единый
#муниципальный тест от 1 до 100 баллов, тип float). Для учеников 2-х и 3-х классов известны
#данные итоговой школьной контрольной по математике (оценки от 1 до 10 баллов, тип float).
#Написать функцию, позволяющую ввести с клавиатуры данные для одного ученика. Используя
#эту функцию, ввести сведения об N учениках и сохранить их в бинарном файле. Распечатать на
#экране содержимое данного файла в виде таблицы.
# Для решения использовать классы, обязательно наличие конструктора(ов),для вывода информации переопределить метод __str__()
#TODO:

"""
Имеется информация об учениках начальной школы.
Для всех учеников известны: фамилия, имя и класс.
Для учеников 1-х классов дополнительно известна их скорость чтения 
(слов в минуту, тип int).
Для учеников 4-х классов известны баллы итоговой аттестации
(единый муниципальный тест от 1 до 100 баллов, тип float).
Для учеников 2-х и 3-х классов известны
данные итоговой школьной контрольной по математике
(оценки от 1 до 10 баллов, тип float).
Написать функцию, позволяющую ввести с клавиатуры данные
для одного ученика.
Используя эту функцию, ввести сведения об N учениках
и сохранить их в бинарном файле. 
Распечатать на экране содержимое данного файла в виде таблицы.
Для решения использовать классы, обязательно наличие конструктора(ов),
для вывода информации переопределить метод __str__()
"""

import pickle

# FIXME: пустая строка между функциями
# TODO:
class Student:
    def __init__(self, last_name, first_name, grade):
        self.last_name = last_name
        self.first_name = first_name
        self.grade = grade
        
    def __str__(self):
        return f"{self.last_name} | {self.first_name} | {self.grade}"


# FIXME: 2 пустые строки между классами
# FIXME: пустая строка между функциями
# TODO:
class FirstGrade(Student):
    def __init__(self, last_name, first_name, grade, reading_speed):
        super().__init__(last_name, first_name, grade)
        self.reading_speed = reading_speed
        
    def __str__(self):
        return f"{super().__str__()} | {self.reading_speed}"


# FIXME: 2 пустые строки между классами
# FIXME: пустая строка между функциями
# TODO:
class FourthGrade(Student):
    def __init__(self, last_name, first_name, grade, test_score):
        super().__init__(last_name, first_name, grade)
        self.test_score = test_score
        
    def __str__(self):
        return f"{super().__str__()} | {self.test_score}"


# FIXME: 2 пустые строки между классами
# FIXME: пустая строка между функциями
class SecondThirdGrade(Student):
    def __init__(self, last_name, first_name, grade, math_score):
        super().__init__(last_name, first_name, grade)
        self.math_score = math_score
        
    def __str__(self):
        return f"{super().__str__()} | {self.math_score}"
    

# FIXME: docstring
# TODO:
def input_student():
    """
    Вводит данные одного ученика с клавиатуры.

    :return: Экземпляр соответствующего класса или None при ошибке
    """
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    grade = int(input("Введите класс (1-4): "))
    if grade == 1:
        reading_speed = int(input("Введите скорость чтения (слов в минуту): "))
        return FirstGrade(last_name, first_name, grade, reading_speed)
    elif grade in [2, 3]:
        math_score = float(input("Введите вещественную оценку за контрольную по математике (от 1 до 10): "))
        return SecondThirdGrade(last_name, first_name, grade, math_score)
    elif grade == 4:
        test_score = float(input("Введите баллы итоговой аттестации (1-100): "))
        return FourthGrade(last_name, first_name, grade, test_score)
    else:
        print('Неверный класс')
        return None


# FIXME: 2 пустые строки между функциями 
# FIXME: docstring
# TODO:
def write_students(students, filename):
    """
    Сохраняет список учеников в бинарный файл.

    :param students: Список объектов учеников
    :param filename: Имя файла для сохранения
    :return: Записывает данные в файл 
    """
    with open(filename, 'wb') as file:
        pickle.dump(students, file)
    print(f'Данные записаны в файл {filename}')
    
    
# FIXME: 2 пустые строки между функциями 
# FIXME: docstring
# TODO:
def read_students(filename):
    with open(filename, 'rb') as file:
        students = pickle.load(file)
    return students


# FIXME: 2 пустые строки между функциями 
# FIXME: docstring
# TODO:
def print_students(students):
    """
    Загружает список учеников из бинарного файла.

    :param filename: Имя файла для чтения
    :return: Список объектов учеников
    """
    print('-------------------------------------------------------------')
    print('|    Фамилия    |    Имя    | Класс |   Доп. информация   |')
    print('-------------------------------------------------------------')
    for student in students:
# FIXME: длина строки больше 79 символов
# TODO:
        print(f'| {student.last_name: <13} | {student.first_name: <10}\
            | {student.grade: <5} | {student} |')
    print('-------------------------------------------------------------')

n = int(input("Введите количество учеников: "))
students = []
for i in range(n):
    print(f'Введите данные для ученика {i + 1}: ')
    student = input_student()
    if student:
        students.append(student)
filename = 'laba15n2.bin'

# FIXME: пустая строка перед вызовом функции
write_students(students, filename)
read_student = read_students(filename)
print(f"Содержимое файла {filename}: ")
print_students(read_student)