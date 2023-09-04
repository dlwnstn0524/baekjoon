from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    l = list(map(int, input()))
    graph.append(l)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append((0,0))
while q:
    x, y = q.popleft()
    for ddx, ddy in zip(dx, dy):
        nx = x + ddx
        ny = y + ddy
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[N-1][M-1])