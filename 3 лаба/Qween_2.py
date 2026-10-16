"""CalcTree3. В текстовом файле с именем filename дано арифметическое
выражение в обратной польской записи. Операндами в выражении являются
целые числа из промежутка от 0 до 9. Используемые операции: сложение(+),
вычитание(-), умножение(*), деление нацело (/) и целочисленный остаток
от деления (%). Постройте дерево, соответствующее данному выражению.
Знаки операций кодируйте числами: сложение (-1), вычитание (-2),
умножение (-3), деление нацело (-4) и целочисленный остаток от деления
(-5). Преобразуйте дерево так, чтобы в нем не было операции умножения
(замените поддеревья, в которых есть умножение значением данного
поддерева). Выведите указатель на корень полученного дерева.
"""

import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)

# FIXME: Добавлен docstring модуля (полный текст условия задачи)
# FIXME: Добавлен импорт logging (стандарт: логирование вместо print)
# FIXME: Добавлен импорт Optional для аннотаций типов
# FIXME: Добавлена пустая строка после импортов

OP_MAP = {"+": -1, "-": -2, "*": -3, "/": -4, "%": -5}
# FIXME: Вынесена константа OP_MAP на уровень модуля
# FIXME: Знаки операций кодируются числами: + → -1, - → -2, * → -3,
#        / → -4, % → -5 (по условию задачи)


class Node:
    """Узел дерева выражения.

    :param value: Значение узла (0–9 для операндов, -1..-5 для операций).
    """

    # FIXME: Добавлен docstring класса
    def __init__(self, value: int) -> None:
        # FIXME: Добавлены аннотации типов
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


def get_op_value(op: str) -> int:
    """Кодирует знак операции согласно условию.

    :param op: Символ операции.
    :return: Отрицательный код операции или 0, если операция неизвестна.
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    # FIXME: Цепочка if заменена на словарь OP_MAP
    return OP_MAP.get(op, 0)


def evaluate(left_val: int, right_val: int, op: int) -> int:
    """Вычисляет результат арифметической операции.

    :param left_val: Левый операнд.
    :param right_val: Правый операнд.
    :param op: Код операции (-1..-5).
    :return: Результат операции.
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    if op == -1:
        return left_val + right_val
    if op == -2:
        return left_val - right_val
    if op == -3:
        return left_val * right_val
    if op == -4:
        return left_val // right_val
    if op == -5:
        return left_val % right_val
    return left_val
    # FIXME: Добавлен return по умолчанию (защита от None)


def simplify(node: Optional[Node]) -> Optional[Node]:
    """Рекурсивно удаляет умножение, заменяя его значением.

    :param node: Корень поддерева.
    :return: Корень упрощённого поддерева.
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    if node is None:
        return None

    node.left = simplify(node.left)
    node.right = simplify(node.right)

    if node.value == -3:
        result = evaluate(node.left.value, node.right.value, -3)
        node.value = result
        node.left = None
        node.right = None
        # FIXME: Заменяем поддерево с умножением значением (по условию)

    return node


def build_and_simplify_tree(filename: str) -> Optional[Node]:
    """Считывает файл, строит дерево и упрощает его.

    :param filename: Путь к файлу с выражением в ОПН.
    :return: Корень преобразованного дерева или None при ошибке.
    :raises FileNotFoundError: Если файл не найден.
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    # FIXME: Добавлена обработка FileNotFoundError
    try:
        with open(filename, "r", encoding="utf-8") as f:
            tokens = f.read().split()
    except FileNotFoundError:
        logging.error("Файл '%s' не найден.", filename)
        return None

    stack: list[Node] = []
    for token in tokens:
        if token.isdigit():
            stack.append(Node(int(token)))
        else:
            op_val = get_op_value(token)
            if op_val != 0:
                right_child = stack.pop()
                left_child = stack.pop()
                node = Node(op_val)
                node.left = left_child
                node.right = right_child
                stack.append(node)

    if not stack:
        return None

    root = stack[0]
    return simplify(root)


def main() -> None:
    """Точка входа: строит дерево, упрощает, выводит указатель.

    :return: None
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлена аннотация возвращаемого типа
    # FIXME: print заменён на logging.info
    filename = "filename"
    root = build_and_simplify_tree(filename)
    if root:
        logging.info("Указатель на корень дерева (id): %s", id(root))
        logging.info("Значение в корне: %s", root.value)
        # FIXME: Выводим id(root) — в Python это аналог указателя
    else:
        logging.warning("Не удалось построить дерево.")


if __name__ == "__main__":
    main()
