T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    
    answer = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                flag1 = True
                flag2 = True
                for k in range(1, K+1):
                    if i + k <= N - 1:
                        if maps[i+k][j] != 1:
                            flag1 = False
                    if j + k <= N - 1:
                        if maps[i][j+k] != 1:
                            flag2 = False
                if flag1:
                    answer += 1
                if flag2:
                    answer += 1
    print("#{} {}".format(test_case, answer))
