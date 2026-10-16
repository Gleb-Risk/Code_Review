// FIXED: #pragma once заменён на #define guard
#ifndef LAB_4_TIME2_H_
#define LAB_4_TIME2_H_

#include <string>

// FIXED: добавлена пустая строка после блока #include

// Класс времени с двумя конструкторами и запросами компонент.
// FIXME: поле должно быть private: seconds_
class Time2 {
 public:
  // FIXED: добавлен explicit, параметр s -> seconds
  explicit Time2(int seconds);

  // FIXED: параметры h -> hours, m -> minutes, s -> seconds
  Time2(int hours, int minutes, int seconds);

  // FIXED: добавлен [[nodiscard]] — значение нельзя игнорировать
  [[nodiscard]] int hour() const;
  [[nodiscard]] int minute() const;
  [[nodiscard]] int second() const;

  // Возвращает время в формате H:MM:SS.
  std::string str() const;
  // Печатает время.
  void print() const;

  // FIXME: по код-стайлу должно быть private: seconds_
  int seconds;
};

#endif  // LAB_4_TIME2_H_
