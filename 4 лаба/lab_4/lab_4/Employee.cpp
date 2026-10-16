#include "Employee.h"

#include <iostream>
// #FIXME: между своей группой include ("Employee.h") и системной
//         (<iostream>) по Google Style должна быть пустая строка:
//             #include "Employee.h"
//             (пустая строка)
//             #include <iostream>
// #FIXME: пустая строка между группой #include и кодом.

Department::Department(std::string t) {
  title = t;
  boss = nullptr;
}

std::string Department::str() const {
  std::string result = "отдел " + title;
  if (boss != nullptr) {
    result += ", начальник " + boss->name;
  }
  return result;
}

void Department::print() const {
  std::cout << str() << "\n";
}

void Department::printStaff() const {
    std::cout << "Сотрудники отдела " << title << ": ";
    for (size_t i = 0; i < staff.size(); i++) {
        std::cout << staff[i]->name;
        if (i + 1 < staff.size()) {
            std::cout << ", ";
        }
    }
    std::cout << "\n";
}


Employee::Employee(std::string n, Department* d) {
  name = n;
  dept = d;
  d->staff.push_back(this);
}

std::string Employee::str() const {
  if (dept->boss == this) {
    return name + " начальник отдела " + dept->title;
  }
  std::string bossName = "(нет)";
  if (dept->boss != nullptr) {
    bossName = dept->boss->name;
  }
  return name + " работает в отделе " + dept->title
    + ", начальник которого " + bossName;
}

void Employee::print() const {
  std::cout << str() << "\n";
}