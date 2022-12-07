import sys

graph = []
blank = []

for i in range(9):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(arr)

for i in range(9) :
    for j in range(9) :
        if graph[i][j] == 0 :
            blank.append((i,j))

def rowOk(a, x) :
    for i in range(9):
        if a == graph[x][i] :
            return False
    return True

def colmnOk(a, y) :
    for i in range(9) :
        if a == graph[i][y] :
            return False
    return True

def rectOk(a, x, y) :
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if a == graph[nx + i][ny +j]:
                return False
    return True

def dfs(idx) :
    if idx == len(blank) :
        for i in range(9) :
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        if rowOk(i, x) and colmnOk(i, y) and rectOk(i, x, y):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)