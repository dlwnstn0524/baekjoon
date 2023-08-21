from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))
    while q:
        sub_sum, idx = q.popleft()
        idx += 1
        if idx == len(numbers):
            if sub_sum == target:
                answer += 1
        else:
            q.append((sub_sum + numbers[idx], idx))
            q.append((sub_sum - numbers[idx], idx))
    return answer