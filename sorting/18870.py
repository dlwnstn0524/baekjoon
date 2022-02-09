n = int(input())
result = [0 for i in range(n)]
cnt = 0

locs= list(map(int, (input().split(' ')))) #입력 완료

for i in range(len(locs)):
    for j in range(len(locs)):
        if locs[i] > locs[j]:
            cnt += 1
    result[i] = cnt
    cnt = 0

print(result)