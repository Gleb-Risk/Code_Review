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

# FIXME: Добавлен docstring модуля (полный текст условия задачи)
# FIXME: Добавлен импорт logging (стандарт: логирование вместо print)
# FIXME: Добавлена пустая строка после импортов


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


def get_plural_word(count: int) -> str:
    """Возвращает правильное склонение слова «попытка».

    :param count: Количество попыток.
    :return: 'попытка', 'попытки' или 'попыток'.
    """
    # FIXME: Добавлена функция склонения (в исходнике всегда «попыток»)
    # FIXME: Добавлены аннотации типов
    last_digit = count % 10
    last_two_digits = count % 100
    if last_digit == 1 and last_two_digits != 11:
        return "попытка"
    if 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return "попытки"
    return "попыток"


def main() -> None:
    """Запрашивает слово и выводит перестановки до совпадения.

    :return: None
    """
    # FIXME: Добавлен docstring
    # FIXME: Добавлена аннотация возвращаемого типа
    # FIXME: Добавлена проверка пустого ввода
    original_word = input("Введите слово: ").strip()
    if not original_word:
        logging.warning("Слово не может быть пустым.")
        return

    attempts = 0
    logging.info("Процесс перестановки:")
    # FIXME: print заменён на logging.info
    while True:
        shuffled_word = shuffle_word(original_word)
        attempts += 1
        logging.info(shuffled_word)
        if shuffled_word == original_word:
            break

    plural = get_plural_word(attempts)
    logging.info("%d %s", attempts, plural)
    # FIXME: Добавлено правильное склонение слова «попытка»


if __name__ == "__main__":
    main()
