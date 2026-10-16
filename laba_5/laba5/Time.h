#ifndef TIME_H_
#define TIME_H_

#include <iostream>

class Time {
public:
    /// @brief Конструктор по умолчанию.
    /// Инициализирует время значением 00:00.
    Time();

    /// @brief Конструктор копирования.
    /// @param time Исходный объект для копирования.
    Time(const Time& time);

    /// @brief Конструктор с параметрами.
    /// Время приводится к диапазону одних суток.
    /// @param hours Количество часов.
    /// @param minutes Количество минут.
    Time(short hours, short minutes);

    /// @brief Возвращает количество часов.
    /// @return Часы в диапазоне [0, 23].
    [[nodiscard]] short GetHours() const;

    /// @brief Возвращает количество минут.
    /// @return Минуты в диапазоне [0, 59].
    [[nodiscard]] short GetMinutes() const;

    /// @brief Вычитает заданное время из текущего.
    /// Учитывается переход в предыдущие сутки.
    /// @param other Вычитаемое время.
    /// @return Результат вычитания типа Time.
    [[nodiscard]] Time Subtract(const Time& other) const;

    /// @brief Префиксный инкремент (добавляет одну минуту).
    /// @return Ссылка на измененный объект.
    Time& operator++();

    /// @brief Постфиксный инкремент (добавляет одну минуту).
    /// @return Копия объекта до изменения.
    Time operator++(int);

    /// @brief Префиксный декремент (вычитает одну минуту).
    /// @return Ссылка на измененный объект.
    Time& operator--();

    /// @brief Постфиксный декремент (вычитает одну минуту).
    /// @return Копия объекта до изменения.
    Time operator--(int);

    /// @brief Неявное приведение к int.
    /// @return Время в минутах.
    operator int() const;

    /// @brief Явное приведение к bool.
    /// @return true, если часы и минуты не равны нулю.
    explicit operator bool() const;

    /// @brief Вывод времени в поток в формате «Время: ЧЧ:ММ».
    /// @param out Поток вывода.
    /// @param time Выводимый объект.
    /// @return Ссылка на поток вывода.
    friend std::ostream& operator<<(std::ostream& out, const Time& time);

private:
    short hours_ = 0;
    short minutes_ = 0;
};

/// @brief Сравнение времени в минутах (меньше).
/// @param left Левый операнд.
/// @param right Правый операнд.
/// @return true, если минут в левом операнде меньше, чем в правом.
[[nodiscard]] bool operator<(const Time& left, const Time& right);

/// @brief Сравнение времени в минутах (больше).
/// @param left Левый операнд.
/// @param right Правый операнд.
/// @return true, если минут в левом операнде больше, чем в правом.
[[nodiscard]] bool operator>(const Time& left, const Time& right);

#endif
