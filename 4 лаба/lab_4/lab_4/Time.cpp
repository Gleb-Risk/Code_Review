#include "Time.h"

// FIXED: добавлена пустая строка между своей группой include
//        и системной
#include <iostream>

// FIXED: добавлена пустая строка после блока #include

namespace {
// FIXED: магические числа заменены именованными константами
constexpr int kSecondsPerDay = 86400;
constexpr int kSecondsPerHour = 3600;
constexpr int kSecondsPerMinute = 60;
}  // namespace

// FIXED: инициализация вынесена в список инициализации,
//        параметр s -> seconds
Time::Time(int seconds) : seconds(seconds) {}

std::string Time::str() const {
  // FIXED: магические числа заменены константами
  int total = seconds % kSecondsPerDay;

  int h = total / kSecondsPerHour;
  int m = (total % kSecondsPerHour) / kSecondsPerMinute;
  int s = total % kSecondsPerMinute;

  std::string result;
  result += std::to_string(h) + ":";
  if (m < 10) {
    result += "0";
  }
  result += std::to_string(m) + ":";
  if (s < 10) {
    result += "0";
  }
  result += std::to_string(s);

  return result;
}

void Time::print() const {
  std::cout << str() << "\n";
}
