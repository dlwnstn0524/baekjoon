from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[0] * n for _ in range(n)]
for i in range(m):
    s, e = map(int, input().split())
    graph[s-1][e-1] = 1 
    graph[e-1][s-1] = 1

visited = [False] * n
flag = False
q = deque()
q.append((x-1, 0))
visited[x-1] = True
while q:
    node, cnt = q.popleft()
    if node == y-1:
        print(cnt)
        flag = True
        break
    for i in range(n):
        if graph[node][i] == 1 and not visited[i]:
            q.append((i, cnt+1))
            visited[i] = True
if not flag:
    print(-1)