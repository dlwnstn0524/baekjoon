from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]
def bfs(i, j, distance):
    q = deque()
    q.append([i, j, distance])
    visited[i][j] = True
    while q:
        i, j, distance = q.popleft()
        if i == n - 1 and j == m - 1:
            return distance
        for ddx, ddy in zip(dx, dy):
            ni, nj = i + ddx, j + ddy
            if 0<= ni < n and 0<= nj < m and visited[ni][nj] == False and graph[ni][nj] == 1:
                q.append([ni, nj, distance +1])
                visited[ni][nj] = True
            else:
                continue
print(bfs(0,0,1))