T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    M = 0
    for i in range(len(prices)-1, -1, -1):
        if prices[i] > M :
            M = prices[i]
        else:
            total += M - prices[i]
    print(total)