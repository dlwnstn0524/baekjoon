from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([1, numbers[0]])
    q.append([1, -numbers[0]])
    while q:
        idx, value = q.popleft()
        if idx == n:
            if value == target:
                answer += 1
            else:
                continue
        else:
            q.append([idx+1, value + numbers[idx]])
            q.append([idx+1, value - numbers[idx]])
    return answer