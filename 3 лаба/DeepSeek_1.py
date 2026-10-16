"""Ввести с клавиатуры любое слово. Используя генерацию случайных чисел,
переставить буквы этого слова в случайном порядке.
Делать это до тех пор, пока полученное слово не совпадёт
с начальным словом. Выводить слово после каждой перестановки и посчитать
общее количество выведенных слов (не считая исходного). 
Пример выполнения программы:
Введите слово: корова
воакро
вокроа
ароовк
краоов
крваоо
оокавр
ооквра
вкраоо
корова
9 попыток
"""

import logging
import random

logging.basicConfig(level=logging.INFO)

# FIXME: Добавлен docstring модуля
# FIXME: Добавлен импорт logging (стандарт: логирование вместо print)
# FIXME: Добавление пустой строки после импортов


def shuffle_word(word: str) -> str:
    """Возвращает случайную перестановку букв слова.

    :param word: Исходное слово.
    :return: Строка с перемешанными буквами.
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def pluralize_attempts(count: int) -> str:
    """Возвращает правильную форму слова «попытка» для числа.

    :param count: Количество попыток.
    :return: 'попытка', 'попытки' или 'попыток'.
    """
    # FIXME: Добавлена функция склонения (в исходнике всегда «попыток»)
    last_digit = count % 10
    last_two = count % 100
    if last_digit == 1 and last_two != 11:
        return "попытка"
    if 2 <= last_digit <= 4 and not (12 <= last_two <= 14):
        return "попытки"
    return "попыток"


def main() -> None:
    """Точка входа: запрашивает слово и перемешивает его.

    :return: None
    """
    # FIXME: Добавлен docstring
    # FIXME: Добавлена аннотация возвращаемого типа
    # FIXME: Добавлена проверка пустого ввода
    word = input("Введите слово: ").strip()
    if not word:
        logging.warning("Слово не может быть пустым.")
        return

    attempts = 0
    while True:
        shuffled = shuffle_word(word)
        logging.info(shuffled)
        # FIXME: print заменён на logging.info
        attempts += 1
        if shuffled == word:
            break

    logging.info("%d %s", attempts, pluralize_attempts(attempts))
    # FIXME: Добавлено правильное склонение слова «попытка»


if __name__ == "__main__":
    main()
