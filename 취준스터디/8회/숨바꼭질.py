from collections import deque

n, k = map(int, input().split())
M = 100000
location = [0] * (M + 1)
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(location[k])
        break
    for nx in (x-1, x+1, 2*x):
        if 0<= nx <= M and location[nx] == 0:
            location[nx] = location[x] + 1
            q.append(nx)