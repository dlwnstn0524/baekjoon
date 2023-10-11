from collections import deque

def solution(s, e):
    answer = 0
    geo = [False] * 10001
    geo[s] = True
    q = deque()
    q.append((s, 0))
    dc = [-1, 1, 5]
    while q:
        coordi, cnt = q.popleft()
        if coordi == e:
            answer = cnt
            break
        else:
            for i in dc:
                n_coordi = i + coordi
                if 1 <= n_coordi <= 10000 and not geo[n_coordi]:
                    q.append((n_coordi, cnt+1))
                    geo[n_coordi] = True
    return answer