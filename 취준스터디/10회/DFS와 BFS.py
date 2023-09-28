from collections import deque

N, M, V = map(int, input().split())
visited_b = [False] * (N+1)
visited_d = [False] * (N+1)
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e], graph[e][s] = 1, 1

def dfs(V):
    global visited_d
    print(V, end= " ")
    visited_d[V] = True
    for i in range(1, N+1):
        if not visited_d[i] and graph[V][i] == 1:
            dfs(i)
    


def bfs(V):
    q = deque()
    q.append(V)
    visited_b[V] = True
    while q:
        v = q.popleft()
        print(v, end= " ")
        for i in range(1, N+1):
            if graph[v][i] == 1 and not visited_b[i]:
                q.append(i)
                visited_b[i]= True

dfs(V)
print()
bfs(V)