def solve():
    # Чтение данных из файла
    with open('FileName.txt', 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    adj_matrix = []
    for line in lines[1:n+1]:
        row = list(map(int, line.strip().split()))
        adj_matrix.append(row)

    # Ввод города K и количества пересадок L
    K = int(input("Введите номер города K: ")) - 1  # Переводим в 0-индексацию
    L = int(input("Введите минимальное количество пересадок L: "))

    # Матрица для хранения кратчайших путей (по количеству рёбер)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                dist[i][j] = 1  # Расстояние = 1 (прямой перелёт)

    # Алгоритм Флойда-Уоршелла (для всех пар вершин)
    for k_city in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k_city] + dist[k_city][j] < dist[i][j]:
                    dist[i][j] = dist[i][k_city] + dist[k_city][j]

    # Поиск городов с не менее чем L+1 пересадками (количество рёбер >= L+2)
    # Так как пересадка = количество рёбер - 1, то для L пересадок нужно рёбер >= L+1
    candidate_cities = []
    for j in range(n):
        if dist[K][j] != float('inf') and dist[K][j] >= L + 1:
            candidate_cities.append(j + 1)  # Возвращаем 1-индексацию

    # Проверим, что для этих городов нет более коротких путей
    # Если кратчайший путь >= L+1, то таких городов и так нет, так как мы уже отфильтровали
    # Но нам нужно убедиться, что нет путей короче L+1 рёбер

    # Если таких городов нет, выводим -1
    if not candidate_cities:
        print(-1)
    else:
        candidate_cities.sort()
        print(' '.join(map(str, candidate_cities)))

# Запуск функции
solve()
