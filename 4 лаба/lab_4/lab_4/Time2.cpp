#include "Time2.h"

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

// FIXED: инициализация вынесена в список инициализации
Time2::Time2(int seconds) : seconds(seconds) {}

// FIXED: делегирующий конструктор, параметры переименованы,
//        магические числа заменены константами
Time2::Time2(int hours, int minutes, int seconds)
    : Time2(hours * kSecondsPerHour + minutes * kSecondsPerMinute + seconds) {}

int Time2::hour() const {
  return (seconds % kSecondsPerDay) / kSecondsPerHour;
}

int Time2::minute() const {
  return (seconds % kSecondsPerHour) / kSecondsPerMinute;
}

int Time2::second() const {
  return seconds % kSecondsPerMinute;
}

std::string Time2::str() const {
  std::string result;
  result += std::to_string(hour()) + ":";
  if (minute() < 10) {
    result += "0";
  }
  result += std::to_string(minute()) + ":";
  if (second() < 10) {
    result += "0";
  }
  result += std::to_string(second());
  return result;
}

void Time2::print() const {
  std::cout << str() << "\n";
}
