from itertools import combinations

N, M = map(int, input().split())

chicken = []
house = []

for i in range(N):
    m = list(map(int, input().split()))
    for j in range(N):
        if m[j] == 1 :
            house.append([i,j])
        elif m[j] == 2:
            chicken.append([i,j])

dis = 9999999

for chi in combinations(chicken, M):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0])+ abs(h[1]- chi[j][1]))
        temp += chi_len
    dis = min(dis, temp)
print(dis)


