from collections import deque

n = int(input())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    board.append(list(map(int, input().rstrip())))
def BFS(board, x,y):

    q = deque()
    q.append((x,y))
    board[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 :
                board[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

count = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            count.append(BFS(board, i, j))

count.sort()
print(len(count))
for i in count:
    print(i)
