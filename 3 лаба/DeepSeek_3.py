from collections import deque

def find_cities(filename, k, l):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
    
    dist = [-1] * n
    start = k - 1
    dist[start] = 0
    q = deque([start])
    
    while q:
        u = q.popleft()
        for v in range(n):
            if matrix[u][v] == 1 and dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    result = []
    for i in range(n):
        if dist[i] == l + 1:  
            result.append(i + 1)
    
    if not result:
        return -1
    return sorted(result)


if __name__ == "__main__":
    result = find_cities("example.txt", 1, 1)
    print(result)  # [4]
