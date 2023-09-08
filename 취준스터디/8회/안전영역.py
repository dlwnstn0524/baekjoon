from collections import deque

N = int(input())
geo = []
M = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    geo.append(temp)
    M = max(temp + [M])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b, value, visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if geo[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = 0
for i in range(M):
    visited = [[0] * N for i in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if geo[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1
    if result < cnt:
        result = cnt
print(result)