def dfs(idx, computers, visited):
    stack = [idx]
    while stack:
        i = stack.pop()
        visited[i] = True
        for j in range(len(computers)):
            if visited[j] == False and computers[idx][j] == 1:
                stack.append(j)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    while False in visited:
        for i in range(n):
            if visited[i] == False:
                dfs(i, computers, visited)
                answer += 1
    return answer