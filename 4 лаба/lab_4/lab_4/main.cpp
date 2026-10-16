// FIXED: порядок #include приведён к код-стайлу:
//        сначала системные, потом стандартные C++,
//        потом заголовки проекта (по алфавиту).
#include <windows.h>

#include <iostream>

#include "Employee.h"
#include "Name.h"
#include "Time.h"
#include "Time2.h"

// FIXED: добавлена пустая строка после блока #include
//        перед int main()

int main() {
  SetConsoleOutputCP(65001);

  // ---------- Задание 1.3. Имена ----------
  std::cout << "===== Задание 1.3. Имена =====\n";
  // FIXED: n1..n3 заменены осмысленными именами
  Name cleopatra("", "Клеопатра", "");
  Name pushkin("Пушкин", "Александр", "Сергеевич");
  Name mayakovsky("Маяковский", "Владимир", "");
  cleopatra.print();
  pushkin.print();
  mayakovsky.print();

  // ---------- Задание 1.4. Время ----------
  std::cout << "\n===== Задание 1.4. Время =====\n";
  // FIXED: t1..t3 заменены осмысленными именами
  Time time_10s(10);
  Time time_10000s(10000);
  Time time_100000s(100000);
  time_10s.print();
  time_10000s.print();
  time_100000s.print();

  // ---------- Задание 2.4. Сотрудники и отделы ----------
  std::cout << "\n===== Задание 2.4. Сотрудники и отделы =====\n";
  Department it("IT");
  Employee petrov("Петров", &it);
  Employee kozlov("Козлов", &it);
  Employee sidorov("Сидоров", &it);
  it.boss = &kozlov;

  petrov.print();
  kozlov.print();
  sidorov.print();

  // ---------- Задание 3.4. Список сотрудников отдела ----------
  std::cout << "\n===== Задание 3.4. Список сотрудников отдела =====\n";
  it.printStaff();

  // ---------- Задание 4.4. Время (два конструктора) ----------
  std::cout << "\n===== Задание 4.4. Время (два конструктора) =====\n";
  // FIXED: a, b заменены осмысленными именами
  Time2 time_from_seconds(10000);
  Time2 time_from_hms(2, 3, 5);
  time_from_seconds.print();
  time_from_hms.print();

  // ---------- Задание 5.4. Запросы ко времени ----------
  std::cout << "\n===== Задание 5.4. Запросы ко времени =====\n";
  // FIXED: x, y, z заменены осмысленными именами
  Time2 time_34056(34056);
  Time2 time_4532(4532);
  Time2 time_1235(1235);

  std::cout << "Время 34056 -> час: " << time_34056.hour() << "\n";
  std::cout << "Время 4532  -> минут с начала часа: "
            << time_4532.minute() << "\n";
  std::cout << "Время 1235  -> секунд с начала минуты: "
            << time_1235.second() << "\n";

  return 0;
}
