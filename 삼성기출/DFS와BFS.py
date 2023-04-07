from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visitied_dfs = [0] * (n+1)
visitied_bfs = [0] * (n+1)

def dfs(v):
    visitied_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if graph[v][i] == 1 and visitied_dfs[i] == 0:
            dfs(i)

def bfs(v):
    q = deque([v])
    visitied_bfs[v] = 1
    while q:
        vertex = q.popleft()
        print(vertex, end=" ")
        for i in range(1, n+1):
            if visitied_bfs[i] == 0 and graph[vertex][i] == 1:
                q.append(i)
                visitied_bfs[i] = 1
dfs(v)
print()
bfs(v)