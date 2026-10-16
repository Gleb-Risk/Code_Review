// FIXED: #pragma once заменён на #define guard
#ifndef LAB_4_TIME_H_
#define LAB_4_TIME_H_

#include <string>

// FIXED: добавлена пустая строка после блока #include

// Класс для хранения времени в секундах.
// FIXME: поле должно быть private: seconds_
class Time {
 public:
  // FIXED: добавлен explicit, параметр s -> seconds
  explicit Time(int seconds);

  // Возвращает время в формате H:MM:SS.
  std::string str() const;
  // Печатает время.
  void print() const;

  // FIXME: по код-стайлу должно быть private: seconds_
  int seconds;
};

#endif  // LAB_4_TIME_H_
