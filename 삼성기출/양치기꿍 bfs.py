from collections import deque


R, C = map(int, input().split())
board = []
visited = [[0] * C for _ in range(R)]

for _ in range(R):
    board.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
def BFS(x, y):
    global w, s
    visited[x][y] = 1
    q.append([x,y])
    while q:
        x, y = q.popleft()
        if board[x][y] == "v":
            w += 1
        if board[x][y] == "k":
            s += 1
        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != "#" and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
wolf = 0
sheep = 0
for i in range(R):
    for j in range(C):
        if board[i][j] != "#" and visited[i][j] == 0:
            w = 0
            s = 0
            BFS(i,j)
            if w >= s :
                s = 0
            else:
                w = 0
            wolf += w
            sheep += s
print(sheep, wolf)
