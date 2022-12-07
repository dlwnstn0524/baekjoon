import sys

graph = []
blank = []

for i in range(9) :
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(9) :
    for j in range(9) :
        if graph[i][j] == 0 :
            blank.append([i,j])

def checkRow(x, a) :
    for i in range(9) :
        if a == graph[x][i]:
            return False
    return True

def checkColmn(y, a) :
    for i in range(9) :
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if graph[nx + i][ny + j] == a :
                return False
    return True

def dfs(idx) :
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        return

    x = blank[idx][0]
    y = blank[idx][1]

    for i in range(1, 10) :
        if checkRow(x, i) and checkColmn(y, i) and checkRect(x, y , i) :
            graph[x][y] = i
            dfs(idx+1)
dfs(0)