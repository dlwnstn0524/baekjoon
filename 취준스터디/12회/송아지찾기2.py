from collections import deque

def solution(s, e):
    answer = 0
    geo = [-1] * 10001
    dx = [1, -1, 5]
    q = deque()
    q.append(s)
    geo[s] = 0
    while q:
        idx = q.popleft()
        if idx == e:
            answer = geo[idx]
            break
        else:
            for ddx in dx:
                n_idx = ddx + idx
                if 0 <= n_idx <= 10000 and geo[n_idx] == -1:
                    q.append(n_idx)
                    geo[n_idx] = geo[idx] + 1
    return answer