from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

visited[0][0] = 1
q = deque()
q.append([0, 0, 1])
while q:
    i, j, distance = q.popleft()
    if i == n - 1 and j == m - 1:
        print(distance)
    for ddi, ddj in zip(di, dj):
        ni = ddi + i
        nj = ddj + j
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj]:
            q.append([ni, nj, distance + 1])
            visited[ni][nj] = 1
