import sys
import os
from collections import deque

def solve():
    input_data = []
    
    # Попытка прочитать из файла "FileName" или "FileName.txt", если он существует
    # Это соответствует условию "задана в текстовом файле с именем FileName"
    if os.path.exists("FileName"):
        with open("FileName", "r", encoding="utf-8") as f:
            input_data = f.read().split()
    elif os.path.exists("FileName.txt"):
        with open("FileName.txt", "r", encoding="utf-8") as f:
            input_data = f.read().split()
    else:
        # Иначе читаем из стандартного потока ввода (стандартная практика для олимпиадных задач)
        input_data = sys.stdin.read().split()
        
    if not input_data:
        return
    
    n = int(input_data[0])
    matrix = []
    idx = 1
    
    # Чтение матрицы смежности
    # Обработка как слитных строк (например, "010"), так и разделенных пробелами значений
    for i in range(n):
        if idx >= len(input_data):
            break
        token = input_data[idx]
        if len(token) == n and all(c in '01' for c in token):
            row = [int(c) for c in token]
            idx += 1
        else:
            row = []
            for j in range(n):
                row.append(int(input_data[idx]))
                idx += 1
        matrix.append(row)
    
    if idx >= len(input_data):
        return
        
    K = int(input_data[idx])
    L = int(input_data[idx+1])
    
    # Проверка корректности начального города
    if K < 1 or K > n:
        print("-1")
        return
        
    start = K - 1
    dist = [-1] * n
    dist[start] = 0
    
    # Поиск в ширину (BFS) для нахождения кратчайших путей в невзвешенном графе
    q = deque([start])
    
    while q:
        u = q.popleft()
        for v in range(n):
            if matrix[u][v] == 1 and dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                
    ans = []
    # Количество пересадок на пути из V ребер равно V - 1.
    # Условие "не менее чем с L пересадками" означает, что количество ребер должно быть >= L + 1.
    for i in range(n):
        if dist[i] != -1 and dist[i] >= L + 1:
            ans.append(i + 1)
            
    if not ans:
        print("-1")
    else:
        # Так как мы проходим по i от 0 до n-1, номера городов уже будут в порядке возрастания
        print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()