from collections import deque

def bfs(visited, computers, i):
    n = len(computers)
    q = deque()
    q.append(i)
    visited[i] = True
    
    while q:
        idx = q.popleft()
        for i in range(n):
            if not visited[i] and computers[idx][i] == 1:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    while False in visited:
        for i in range(n):
            if not visited[i]:
                bfs(visited, computers, i)
                answer += 1
    return answer