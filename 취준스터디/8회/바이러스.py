from collections import deque

n = int(input())
visited = [False] * n
graph = [[0] * n for _ in range(n)]

v = int(input())
for i in range(v):
    s, e = map(int, input().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

cnt = 0
q = deque()
q.append(0)
visited[0] = True
while q:
    vertex = q.popleft()
    for i in range(n):
        if not visited[i] and graph[vertex][i] == 1:
            q.append(i)
            cnt += 1
            visited[i] = True
print(cnt)