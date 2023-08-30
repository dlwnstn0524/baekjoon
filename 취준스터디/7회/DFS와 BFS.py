from collections import deque

n, m, v = map(int, input().split())
graph  = [[0] * n for _ in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

# DFS Code
stack = [v-1]
visited = [False] * n
while False in visited:
    i = stack.pop()
    visited[i] = True
    print(i+1, end= " ")
    for j in range(n):
        if graph[i][j] == 1 and visited[j] == False:
            stack.append(j)

# BFS Code
# q = deque([v-1])
# visited = [False] * n
# while q:


