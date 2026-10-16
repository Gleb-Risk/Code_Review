#include "Name.h"

// FIXED: добавлена пустая строка между своей группой include
//        и системной
#include <iostream>

// FIXED: добавлена пустая строка после блока #include

// FIXED: инициализация вынесена в список инициализации,
//        параметры переименованы
Name::Name(std::string surname, std::string first, std::string patronymic)
    : surname(surname), first(first), patronymic(patronymic) {}

std::string Name::str() const {
  std::string result;

  // FIXED: сравнение != "" заменено на !.empty()
  if (!surname.empty()) {
    result += surname;
  }
  if (!first.empty()) {
    // FIXED: исправлены отступы, добавлены фигурные скобки
    if (!result.empty()) {
      result += " ";
    }
    result += first;
  }
  if (!patronymic.empty()) {
    // FIXED: исправлены отступы, добавлены фигурные скобки
    if (!result.empty()) {
      result += " ";
    }
    result += patronymic;
  }

  return result;
}

void Name::print() const {
  std::cout << str() << "\n";
}
