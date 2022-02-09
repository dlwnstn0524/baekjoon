n = int(input())
locs = []
for i in range(n):
    x,y = map(int, input().split())
    locs.append([y,x])
locs.sort()
for y,x in locs:
    print(x, y)