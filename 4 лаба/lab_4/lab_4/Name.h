// FIXED: #pragma once заменён на #define guard
#ifndef LAB_4_NAME_H_
#define LAB_4_NAME_H_

#include <string>

// FIXED: добавлена пустая строка после блока #include

// Класс для хранения ФИО.
// FIXME: поля должны быть private: surname_, first_, patronymic_
class Name {
 public:
  // FIXED: параметры s -> surname, f -> first, p -> patronymic
  Name(std::string surname, std::string first, std::string patronymic);

  // Возвращает ФИО в виде строки.
  std::string str() const;
  // Печатает ФИО.
  void print() const;

  // FIXME: по код-стайлу должны быть private
  std::string surname;
  std::string first;
  std::string patronymic;
};

#endif  // LAB_4_NAME_H_
