from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    q.append([numbers[0], 0])
    q.append([-1*numbers[0], 0])
    while q:
        value, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([value + numbers[idx], idx])
            q.append([value + (-1)*numbers[idx], idx])
        else:
            if value == target:
                answer += 1
    return answer