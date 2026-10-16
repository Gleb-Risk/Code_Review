#include "Time.h"

#include <iostream>
// #FIXME: между своей группой include ("Time.h") и системной
//         (<iostream>) по Google Style должна быть пустая строка:
//             #include "Time.h"
//             (пустая строка)
//             #include <iostream>

Time::Time(int s) {
  seconds = s;
}

std::string Time::str() const {
  int total = seconds % 86400;

  int h = total / 3600;
  int m = (total % 3600) / 60;
  int s = total % 60;

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