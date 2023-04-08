c = int(input())
n = int(input())
graph = [[0] * (c + 1) for _ in range(c + 1)]
visited = [0] * (c + 1)
for _ in range(n):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(v, cnt):
    visited[v] = 1
    for i in range(c + 1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i, cnt + 1)
    return

dfs(1, 0)
print(sum(visited)-1)
