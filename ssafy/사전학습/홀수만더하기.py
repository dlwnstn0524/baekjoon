T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    nums = list(map(int, input().split()))
    for num in nums:
        if num % 2 == 1:
            answer += num
    print("#{} {}".format(test_case, answer))
