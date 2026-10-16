#include "Employee.h"

// FIXED: добавлена пустая строка между своей группой include
//        и системной
#include <iostream>

// FIXED: добавлена пустая строка после блока #include

// FIXED: инициализация вынесена в список инициализации,
//        параметр t -> title
Department::Department(std::string title)
    : title(title), boss(nullptr) {}

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
  // FIXED: отступы приведены к 2 пробелам (было 4)
  std::cout << "Сотрудники отдела " << title << ": ";
  for (size_t i = 0; i < staff.size(); i++) {
    std::cout << staff[i]->name;
    if (i + 1 < staff.size()) {
      std::cout << ", ";
    }
  }
  std::cout << "\n";
}

// FIXED: параметры n -> name, d -> dept,
//        инициализация вынесена в список инициализации
Employee::Employee(std::string name, Department* dept)
    : name(name), dept(dept) {
  // FIXME: нет проверки dept на nullptr — возможное падение.
  dept->staff.push_back(this);
}

std::string Employee::str() const {
  if (dept->boss == this) {
    return name + " начальник отдела " + dept->title;
  }
  // FIXED: bossName -> boss_name (snake_case)
  std::string boss_name = "(нет)";
  if (dept->boss != nullptr) {
    boss_name = dept->boss->name;
  }
  return name + " работает в отделе " + dept->title
      + ", начальник которого " + boss_name;
}

void Employee::print() const {
  std::cout << str() << "\n";
}
