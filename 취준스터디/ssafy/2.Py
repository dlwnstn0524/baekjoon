from collections import Counter
T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    N, A, B = map(int, input().split())
    grades = list(map(int, input().split()))
    counter = Counter(grades)
    value = list(counter.keys())
    value.sort()
    left = 1
    right = len(value) - 2
    temp = 0
    cand = []
    while left <= right:
        for i in value[left:right+1]:
            temp += counter[i]
        if A <= temp <= B:
            cand.append(temp)
            break
        else:
            right -= 1
            left += 1
            temp = 0
    if A <= temp + counter[left-1] <= B and left != 0:
        cand.append(temp + counter[left-1])
    if A <= temp + counter[right+1] <= B and right != len(value):
        cand.append(temp + counter[right+1])
    cand.sort(reverse=True)
    print("#{} {}".format(test_case, cand[0]))
