from collections import Counter

T = int(input())
for test_case in range(T):
    answer_cnt = 0
    answer = 0
    
    t = int(input())
    nums = list(map(int, input().split()))
    counter = Counter(nums)
    
    for key, value in counter.items():
        if value > answer_cnt:
            answer_cnt = value
            answer = key
    print("#{} {}".format(t, answer))
