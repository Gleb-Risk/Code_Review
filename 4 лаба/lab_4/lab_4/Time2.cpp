#include "Time2.h"

#include <iostream>

// #FIXME: между своей группой include ("Employee.h") и системной
//         (<iostream>) по Google Style должна быть пустая строка:
//             #include "Employee.h"
//             (пустая строка)
//             #include <iostream>
// #FIXME: пустая строка между группой #include и кодом.

Time2::Time2(int s) {
  seconds = s;
}

Time2::Time2(int h, int m, int s) : Time2(h * 3600 + m * 60 + s) {
}

int Time2::hour() const {
  return (seconds % 86400) / 3600;
}

int Time2::minute() const {
  return (seconds % 3600) / 60;
}

int Time2::second() const {
  return seconds % 60;
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