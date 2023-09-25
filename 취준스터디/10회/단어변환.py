from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        q = deque()
        q.append((begin, 0))
        visited = [False] * len(words)
        while q:
            now, cnt = q.popleft()
            if now == target:
                return cnt
            for i in range(len(words)):
                if not visited[i]:
                    diff = 0
                    for j in range(len(words[i])):
                        if words[i][j] != now[j]:
                            diff += 1
                if diff == 1:
                    q.append((words[i], cnt+1))
                    visited[i] = True
    return answer