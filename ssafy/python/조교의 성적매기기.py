T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N, K = map(int, input().split())
    scores = []
    rank = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    for i in range(N):
        mid, fin, hom = map(int, input().split())
        scores.append((i, mid*0.35 + fin*0.45 + hom*0.2))
    
    scores.sort(key=lambda x : -x[1])

    for i in range(N):
        if scores[i][0] == K - 1:
            answer = rank[i//(N//10)]
            break
    
    print("#{} {}".format(test_case, answer))