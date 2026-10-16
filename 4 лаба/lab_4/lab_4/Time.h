#pragma once

#include <string>

class Time {
public:
  int seconds;

  Time(int s);

  std::string str() const;
  void print() const;
};