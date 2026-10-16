#include <iostream>
// #FIXME: windows.h отдельной группой
#include <windows.h>          

// #FIXME: свои заголовки надо отсортировать по алфавиту.Google Style
//         требует, чтобы #include шли в алфавитном порядке 
#include "Employee.h"
#include "Name.h"
#include "Time.h"
#include "Time2.h"


int main() {
  SetConsoleOutputCP(65001);   

  // ---------- Задание 1.3 ----------
  std::cout << "===== Задание 1.3. Имена =====\n";
  Name n1("", "Клеопатра", "");
  Name n2("Пушкин", "Александр", "Сергеевич");
  Name n3("Маяковский", "Владимир", "");
  n1.print();
  n2.print();
  n3.print();

  // ---------- Задание 1.4 ----------
  std::cout << "\n===== Задание 1.4. Время =====\n";
  Time t1(10);
  Time t2(10000);
  Time t3(100000);
  t1.print();
  t2.print();
  t3.print();

  // ---------- Задание 2.4 ----------
  std::cout << "\n===== Задание 2.4. Сотрудники и отделы =====\n";
  Department it("IT");
  Employee petrov("Петров", &it);
  Employee kozlov("Козлов", &it);
  Employee sidorov("Сидоров", &it);
  it.boss = &kozlov;

  petrov.print();
  kozlov.print();
  sidorov.print();

  // ---------- Задание 3.4 ----------
  std::cout << "\n===== Задание 3.4. Список сотрудников отдела =====\n";
  it.printStaff();

  // ---------- Задание 4.4 ----------
  std::cout << "\n===== Задание 4.4. Время (два конструктора) =====\n";
  Time2 a(10000);
  Time2 b(2, 3, 5);
  a.print();
  b.print();

  // ---------- Задание 5.4 ----------
  std::cout << "\n===== Задание 5.4. Запросы ко времени =====\n";
  Time2 x(34056);
  Time2 y(4532);
  Time2 z(1235);

  std::cout << "Время 34056 -> час: " << x.hour() << "\n";
  std::cout << "Время 4532  -> минут с начала часа: " << y.minute() << "\n";
  std::cout << "Время 1235  -> секунд с начала минуты: " << z.second() << "\n";

  return 0;
}