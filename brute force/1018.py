m, n = map(int, input().split())

arr = []
min = 64

for i in range(m):
    arr.append(input())

sfw = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
sfb = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
cnt = [[0]*(n-7) for row in range(m-7)]


for i in range(m-7):
    for j in range(n-7):
        if arr[i][j] == 'W' :
            for k in range(8):
                for l in range(8) :
                    if arr[i+k][j+l] != sfw[k][l] :
                        cnt[i][j] += 1
        elif arr[i][j] == 'B' :
            for k in range(8):
                for l in range(8) :
                    if arr[i+k][j+l] != sfb[k][l] :
                        cnt[i][j] += 1

for i in cnt:
    for j in i:
        if min > j :
            min = j

print(min)