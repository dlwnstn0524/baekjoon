from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for ddx, ddy in zip(dx, dy):
            nx = ddx + x
            ny = ddy + y
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx, ny])
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]