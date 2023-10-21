from collections import deque

def bfs(i, computers, visited):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        idx = q.popleft()
        for i in range(len(computers)):
            if not visited[i] and computers[idx][i] == 1:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    while True:
        if False not in visited:
            break
        else:
            for i in range(n):
                if not visited[i]:
                    bfs(i, computers, visited)
                    answer += 1
    return answer