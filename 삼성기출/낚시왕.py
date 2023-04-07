R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    # 순서대로 속력, 방향, 크기. 1 = 위 2 = 아래 3 = 오른  4 = 왼
    board[r][c] = [s, d, z]

def hunt(j):
    for i in range(R):
        if board[i][j]:
            # print(i, j, board[i][j])
            temp = board[i][j][2]
            board[i][j] = 0
            return temp
    return 0


def next_location(i, j, speed, direction):
    if direction == 1 or direction == 2:
        period = 2 * R - 2
        if direction == 2:
            speed += i
        else:
            speed += 2 * R - 2 - i
        speed %= period
        if speed > R - 1:
            return 2 * R - 2 - speed, j, 1
        return speed, j, 2
    if direction == 3 or direction == 4:
        period = 2 * C - 2
        if direction == 3:
            speed += j
        else:
            speed += 2 * C - 2 - j
        speed %= period
        if speed > C - 1:
            return i, 2 * C - 2 - speed, 4
        return i, speed, 3


def fish_move():
    global board
    next_board = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:

                ni, nj, nd = next_location(i, j, board[i][j][0], board[i][j][1])

                if next_board[ni][nj]:
                    next_board[ni][nj] = max(next_board[ni][nj], [board[i][j][0], nd, board[i][j][2]],
                                             key=lambda x: x[2])
                else:
                    next_board[ni][nj] = [board[i][j][0], nd, board[i][j][2]]
    board = next_board


answer = 0
for j in range(C):
    answer += hunt(j)
    fish_move()

print(answer)
