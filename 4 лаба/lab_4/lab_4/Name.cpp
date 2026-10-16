#include "Name.h"

#include <iostream>
// #FIXME: между своей группой include ("Name.h") и системной (<iostream>)
//         по Google Style должна быть пустая строка:
//         #include "Name.h"
//         (пустая строка)
//         #include <iostream>

Name::Name(std::string s, std::string f, std::string p) {
  surname = s;
  first = f;
  patronymic = p;
}

std::string Name::str() const {
  std::string result;

  if (surname != "") {
    result += surname;
  }
  if (first != "") {
    if (result != "") 
    result += " ";
    result += first;
  }
  if (patronymic != "") {
    if (result != "") result += " ";
      result += patronymic;
  }

  return result;
}

void Name::print() const {
  std::cout << str() << "\n";
}
