from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(index, computers, visited):
        q = deque()
        q.append(index)
        visited[index] = True
        while q:
            idx = q.popleft()
            for i in range(len(computers)):
                if not visited[i] and computers[idx][i] == 1:
                    q.append(i)
                    visited[i] = True
        
    for i in range(n):
        if False not in visited:
            break
        if visited[i] == False:
            bfs(i, computers, visited)
            answer += 1
    return answer