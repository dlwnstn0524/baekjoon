from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    
    n = len(maps)
    m = len(maps[0])
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    print(maps)
    return maps[-1][-1] if maps[-1][-1] > 1 else -1
