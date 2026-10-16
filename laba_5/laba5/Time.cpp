#include "Time.h"


namespace {

    const int kMinutesInHour = 60;
    const int kMinutesInDay = 24 * kMinutesInHour;

}


Time::Time() = default;


Time::Time(const Time& time)
    : hours_(time.hours_), minutes_(time.minutes_) {
}


Time::Time(short hours, short minutes) {
    int total = hours * kMinutesInHour + minutes;
    total = ((total % kMinutesInDay) + kMinutesInDay) % kMinutesInDay;
    hours_ = static_cast<short>(total / kMinutesInHour);
    minutes_ = static_cast<short>(total % kMinutesInHour);
}


short Time::GetHours() const {
    return hours_;
}


short Time::GetMinutes() const {
    return minutes_;
}


std::ostream& operator<<(std::ostream& out, const Time& time) {
    out << "Время: ";
    if (time.hours_ < 10) {
        out << '0';
    }
    out << time.hours_ << ":";
    if (time.minutes_ < 10) {
        out << '0';
    }
    out << time.minutes_;
    return out;
}


Time Time::Subtract(const Time& other) const {
    int diff = static_cast<int>(*this) - static_cast<int>(other);
    return Time(0, static_cast<short>(diff));
}


Time& Time::operator++() {
    *this = Time(0, static_cast<short>(static_cast<int>(*this) + 1));
    return *this;
}


Time Time::operator++(int) {
    Time time = *this;
    ++(*this);
    return time;
}


Time& Time::operator--() {
    *this = Time(0, static_cast<short>(static_cast<int>(*this) - 1));
    return *this;
}


Time Time::operator--(int) {
    Time time = *this;
    --(*this);
    return time;
}


Time::operator int() const {
    return hours_ * kMinutesInHour + minutes_;
}


Time::operator bool() const {
    return (hours_ != 0) && (minutes_ != 0);
}


bool operator<(const Time& left, const Time& right) {
    return static_cast<int>(left) < static_cast<int>(right);
}


bool operator>(const Time& left, const Time& right) {
    return static_cast<int>(left) > static_cast<int>(right);
}