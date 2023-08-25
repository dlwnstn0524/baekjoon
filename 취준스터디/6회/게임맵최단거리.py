from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and maps[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx))
                maps[ny][nx] = maps[y][x] + 1
    return -1 if maps[-1][-1] == 1 else maps[-1][-1]