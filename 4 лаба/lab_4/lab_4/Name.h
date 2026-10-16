#pragma once

#include <string>

class Name {
public:
  std::string surname;
  std::string first;
  std::string patronymic;

  Name(std::string s, std::string f, std::string p);

  std::string str() const;
  void print() const;
};