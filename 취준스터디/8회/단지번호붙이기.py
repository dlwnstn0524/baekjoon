from collections import deque

N = int(input())

graph = []
total = 0

for _ in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y,0))
    graph[x][y] = 0
    count = 1
    while q:
        x, y, cnt = q.popleft()
        for ddx, ddy in zip(dx, dy):
            nx = ddx + x
            ny = ddy + y
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                q.append((nx, ny, cnt + 1))
                graph[nx][ny] = 0
                count += 1
    return count
answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
for i in answer:
    print(i)