n = int(input())
locs = []
for i in range(n):
    loc = list(map(int, input().split()))
    locs.append(loc)
locs.sort()
for i in locs:
    print(i[0], i[1])