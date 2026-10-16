#pragma once

#include <string>
#include <vector>
// #FIXME: пустая строка между группой #include и кодом.

class Employee;   

class Department {
public:
  std::string title;
  Employee* boss;
  std::vector<Employee*> staff;

  Department(std::string t);

  std::string str() const;
  void print() const;
  void printStaff() const;   
};

class Employee {
public:
  std::string name;
  Department* dept;

  Employee(std::string n, Department* d);

  std::string str() const;
  void print() const;
};