def dfs(idx, computers, visited):
    stack = [idx]
    while stack:
        index = stack.pop()
        visited[index] = True
        for i in range(len(computers)):
            if visited[i] == False and computers[index][i] == 1:
                stack.append(i)
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if False not in visited:
            break
        else:
            if visited[i] == False:
                dfs(i, computers, visited)
                answer += 1
    return answer