from copy import deepcopy
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def leftmove(param):
    for i in range(n):
        p = 0
        for j in range(1, n):
            if param[i][j]:
                temp = param[i][j]
                param[i][j] = 0
                if param[i][p] == 0:
                    param[i][p] = temp
                elif param[i][p] == temp:
                    param[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    param[i][p] = temp
    return param


def rightmove(param):
    for i in range(n):
        p = n - 1
        for j in range(n -2, -1, -1):
            if param[i][j]:
                temp = param[i][j]
                param[i][j] = 0
                if param[i][p] == 0:
                    param[i][p] = temp
                elif param[i][p] == temp:
                    param[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    param[i][p] = temp
    return param


def upmove(param):
    for j in range(n):
        p = 0
        for i in range(1, n):
            if param[i][j] :
                temp = param[i][j]
                param[i][j] = 0
                if param[p][j] == 0:
                    param[p][j] = temp
                elif param[p][j] == temp:
                    param[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    param[p][j] = temp
    return param


def downmove(param):
    for j in range(n):
        p = n - 1
        for i in range(n - 2, -1, -1):
            if param[i][j]:
                temp = param[i][j]
                param[i][j] = 0
                if param[p][j] == 0:
                    param[p][j] = temp
                elif param[p][j] == temp:
                    param[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    param[p][j] = temp
    return param


def dfs(board, cnt):
    global ans
    if cnt == 5:
        ans = max(ans, max(map(max, board)))
        return

    dfs(leftmove(deepcopy(board)), cnt+1)
    dfs(rightmove(deepcopy(board)), cnt + 1)
    dfs(upmove(deepcopy(board)), cnt + 1)
    dfs(downmove(deepcopy(board)), cnt + 1)

dfs(board, 0)
print(ans)
