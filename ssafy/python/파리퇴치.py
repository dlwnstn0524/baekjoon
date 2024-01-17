T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    answer = 0
    maps = []
    
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(M):
                for l in range(M):
                    ni = i + k
                    nj = j + l
                    if 0 <= ni < N and 0 <= nj < N:
                        temp += maps[ni][nj]
                    else:
                        continue
            answer = max(answer, temp)
            
    print("#{} {}".format(test_case, answer))