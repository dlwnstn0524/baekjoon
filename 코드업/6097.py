h, w = map(int, input().split())
maps = []
for i in range(h):
    maps.append([0]*w)

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            maps[x-1][y-1+j] = 1
    else:
        for j in range(l):
            maps[x-1+j][y-1] = 1
for i in maps:
    for j in i:
        print(j, end=" ")
    print()
