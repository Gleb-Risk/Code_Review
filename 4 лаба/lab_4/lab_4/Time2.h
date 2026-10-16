#pragma once

#include <string>

class Time2 {
public:
  int seconds;

  // задание 4.4 — два конструктора
  Time2(int s);
  Time2(int h, int m, int s);

  // задание 5.4 — запросы
  int hour() const;
  int minute() const;
  int second() const;

  std::string str() const;
  void print() const;
};