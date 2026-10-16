"""Graf8. Юный путешественник решил изучить схему авиационного
сообщения. Схема авиационного сообщения задана в текстовом файле
с именем FileName в виде матрицы смежности. Первая строка файла
содержит количество городов (n) n<=15, связанных авиационным
сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если
не имеется возможности перелета из города i в город j, иначе
m[i][j]=1. Определить номера городов, в которые из города K можно
долететь не менее чем с L пересадками и более коротких путей к таким
городам не существует. Перечислите номера таких городов в порядке
возрастания. Нумерация городов начинается с 1. Если таких городов
нет, выведите число (-1).
"""

import logging
import os
import sys
from collections import deque

logging.basicConfig(level=logging.INFO)

# FIXME: Добавлен docstring модуля (полный текст условия задачи)
# FIXME: Добавлен импорт logging (стандарт: логирование вместо print)
# FIXME: Добавлены импорты os, sys для гибкого чтения
# FIXME: Добавлена пустая строка после импортов


def read_input() -> list[str]:
    """Читает данные из файла FileName или stdin.

    :return: Список токенов.
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлена аннотация возвращаемого типа
    for name in ("FileName", "FileName.txt"):
        if os.path.exists(name):
            with open(name, "r", encoding="utf-8") as f:
                return f.read().split()
    return sys.stdin.read().split()


def parse_matrix(
    tokens: list[str], n: int
) -> tuple[list[list[int]], int]:
    """Разбирает матрицу смежности из токенов.

    :param tokens: Список токенов.
    :param n: Количество вершин.
    :return: Кортеж (матрица, индекс следующего токена).
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    # FIXME: Добавлена обработка слитных и раздельных строк
    matrix: list[list[int]] = []
    idx = 1
    for _ in range(n):
        if idx >= len(tokens):
            break
        token = tokens[idx]
        if len(token) == n and all(c in "01" for c in token):
            matrix.append([int(c) for c in token])
            idx += 1
        else:
            row = [int(tokens[idx + j]) for j in range(n)]
            idx += n
            matrix.append(row)
    return matrix, idx


def bfs_distances(
    start: int, matrix: list[list[int]]
) -> list[int]:
    """Вычисляет кратчайшие расстояния от start.

    :param start: Индекс начальной вершины (0-based).
    :param matrix: Матрица смежности.
    :return: Список расстояний (-1, если вершина недостижима).
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлены аннотации типов
    # FIXME: BFS даёт кратчайшее расстояние — то, что нужно
    #        для условия «нет более коротких путей»
    n = len(matrix)
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in range(n):
            if matrix[u][v] == 1 and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist


def solve() -> None:
    """Читает данные, находит и выводит города.

    :return: None
    """
    # FIXME: Добавлен docstring функции
    # FIXME: Добавлена аннотация возвращаемого типа
    # FIXME: print заменён на logging.info
    tokens = read_input()
    if not tokens:
        return

    n = int(tokens[0])
    matrix, idx = parse_matrix(tokens, n)
    if idx >= len(tokens):
        return

    k = int(tokens[idx])
    l = int(tokens[idx + 1])
    # FIXME: K, L переименованы в k, l (snake_case по стандарту)

    if k < 1 or k > n:
        logging.info("-1")
        return
        # FIXME: Добавлена проверка корректности начального города

    dist = bfs_distances(k - 1, matrix)

    # FIXME: «не менее чем с L пересадками» означает рёбер >= L + 1.
    #        Так как dist — кратчайшее расстояние, условие
    #        dist >= L + 1 автоматически означает «нет более коротких
    #        путей» — это требование Graf8.
    ans = [i + 1 for i in range(n)
           if dist[i] != -1 and dist[i] >= l + 1]

    if not ans:
        logging.info("-1")
    else:
        logging.info(" ".join(map(str, ans)))
        # FIXME: Так как i идёт от 0 до n-1, порядок возрастания
        #        уже обеспечен


if __name__ == "__main__":
    solve()
