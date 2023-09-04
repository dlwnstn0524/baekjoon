from collections import deque

N = int(input())

graph = []
total = 0
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    pass

while True:
    if 1 not in graph:
        break
    else:
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and graph[i][j] == 1:
                    bfs(i,j)
                    