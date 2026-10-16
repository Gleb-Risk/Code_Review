// FIXED: #pragma once заменён на #define guard
#ifndef LAB_4_EMPLOYEE_H_
#define LAB_4_EMPLOYEE_H_

#include <string>
#include <vector>

// FIXED: добавлена пустая строка после блока #include

class Employee;

// Отдел с названием, начальником и списком сотрудников.
// FIXME: поля оставлены public, чтобы не ломать main.cpp.
class Department {
 public:
  // FIXED: добавлен explicit, параметр t -> title
  explicit Department(std::string title);

  // Возвращает строковое представление отдела.
  std::string str() const;
  // Печатает строковое представление отдела.
  void print() const;
  // Печатает список сотрудников отдела.
  void printStaff() const;

  // FIXME: по код-стайлу должны быть private: title_, boss_, staff_
  std::string title;
  Employee* boss;
  std::vector<Employee*> staff;
};

// Сотрудник, привязанный к отделу.
// FIXME: поля оставлены public, чтобы не ломать main.cpp.
class Employee {
 public:
  // FIXED: параметры n -> name, d -> dept
  Employee(std::string name, Department* dept);

  // Возвращает строковое представление сотрудника.
  std::string str() const;
  // Печатает строковое представление сотрудника.
  void print() const;

  // FIXME: по код-стайлу должны быть private: name_, dept_
  std::string name;
  Department* dept;
};

#endif  // LAB_4_EMPLOYEE_H_
