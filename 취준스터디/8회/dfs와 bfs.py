from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):
    visited1[V] = True
    print(V, end= " ")
    for i in range(1, N+1):
        if visited1[i] == False and graph[V][i] == True:
            dfs(i)
def bfs(v):
    q = deque()
    q.append(v)       
    visited2[v] = 1   
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, N + 1):
            if visited2[i] == False and graph[v][i] == True:
                q.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)