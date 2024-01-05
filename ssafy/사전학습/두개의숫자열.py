T = int(input())
for test_case in range(1, T+1):
    answer = 0

    n, m = map(int, input().split())
    if n >= m:
        B = list(map(int, input().split()))
        A= list(map(int, input().split()))
    elif n < m:
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

    #배열 A가 더 짧은 배열
    for i in range(abs(n-m)+1):
        sub_B = B[i:len(A)+i]
        temp = 0
        for j, k in zip(A, sub_B):
            print
            temp += j*k
        if temp > answer:
            answer = temp
    print("#{} {}".format(test_case, answer))