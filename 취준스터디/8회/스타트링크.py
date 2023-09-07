from collections import deque

f, s, g, u, d = map(int, input().split())
floor = [0] * (f+1)
flag = False

q = deque()
q.append(s)
while q:
    x = q.popleft()
    if x == g:
        break
    for nx in (x+u, x-d):
        if 0 <= nx <= f and floor[nx] == 0:
            floor[nx] = floor[x] + 1
            q.append(nx)

if floor[g] == 0 :
    print("use the stairs")
else :
    print(floor[g])