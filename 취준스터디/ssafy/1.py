
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    prices.sort(reverse=True)

    while prices:
        if len(prices) == 1:
            total += prices.pop(0)
            break
        elif len(prices) == 0:
            break
        else:
            if prices[0] != prices[1]:
                total += prices.pop(0)
                prices.pop(0)
            else:
                flag = False
                for i in range(2, len(prices)):
                    if prices[0] != prices[i]:
                        total += prices.pop(0)
                        prices.pop(i-1)
                        flag = True
                        break
                if not flag:
                    total += prices.pop(0)

    print("#{} {}".format(test_case, total))
