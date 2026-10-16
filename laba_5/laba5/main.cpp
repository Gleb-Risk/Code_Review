#include <clocale>

#include <iostream>

#include "Time.h"



void PrintMenu() {
    std::cout << "Вариант 7.\n"
        << "Задача: Реализовать класс Time.\n"
        << "Поля: short int hours, short int minutes "
        << "(часы и минуты)\n"
        << "Методы: Вычитание переменной типа Time "
        << "(с учетом перехода в предыдущие сутки). "
        << "Результат типа Time.\n"
        << "Список действий над объектом:\n"
        << "1. Создать объект.\n"
        << "2. Вычитание переменной типа Time.\n"
        << "3. ++Object (префикс, добавление минуты).\n"
        << "4. Object++ (постфикс, добавление минуты).\n"
        << "5. --Object (префикс, вычитание минуты).\n"
        << "6. Object-- (постфикс, вычитание минуты).\n"
        << "7. Неявное приведение типа int() (время в минутах).\n"
        << "8. Явное приведение типа bool() "
        << "(true, если часы и минуты не равны нулю).\n"
        << "9. Object < Time t (сравнение в минутах).\n"
        << "10. Object > Time t (сравнение в минутах).\n"
        << "-1. Выход\n";
}


Time ReadTime() {
    short hours = 0;
    short minutes = 0;
    std::cout << "Введите часы: ";
    std::cin >> hours;
    std::cout << "Введите минуты: ";
    std::cin >> minutes;
    return Time(hours, minutes);
}


int main(int argc, char* argv[]) {
    setlocale(LC_ALL, "Rus");
    PrintMenu();

    Time obj;
    bool flag = true;

    while (flag) {
        std::cout << "\nТекущий объект: " << obj << "\n"
            << "Введите действие над объектом: ";

        int action = 0;
        std::cin >> action;

        if (action == -1) {
            break;
        }

        switch (action) {
        case 1: {
            obj = ReadTime();
            std::cout << "Создан объект: " << obj << "\n";
            break;
        }
        case 2: {
            std::cout << "Введите вычитаемое время.\n";
            Time other = ReadTime();
            obj = obj.Subtract(other);
            std::cout << "Результат вычитания: " << obj << "\n";
            break;
        }
        case 3: {
            std::cout << ++obj << "\n";
            break;
        }
        case 4: {
            std::cout << obj++ << "\n";
            break;
        }
        case 5: {
            std::cout << --obj << "\n";
            break;
        }
        case 6: {
            std::cout << obj-- << "\n";
            break;
        }
        case 7: {
            int minutes = obj;
            std::cout << "Неявное приведение к int (минуты): "
                << minutes << "\n";
            break;
        }
        case 8: {
            std::cout << "Явное приведение к bool: " << std::boolalpha
                << static_cast<bool>(obj) << "\n";
            break;
        }
        case 9: {
            std::cout << "Введите время для сравнения.\n";
            Time other = ReadTime();
            std::cout << std::boolalpha << (obj < other) << "\n";
            break;
        }
        case 10: {
            std::cout << "Введите время для сравнения.\n";
            Time other = ReadTime();
            std::cout << std::boolalpha << (obj > other) << "\n";
            break;
        }
        default: {
            std::cout << "Такого действия нет\n";
            break;
        }
        }
    }

    return 0;
}