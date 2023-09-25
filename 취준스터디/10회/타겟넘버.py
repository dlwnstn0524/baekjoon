from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    q.append([0, numbers[0]])
    q.append([0, -numbers[0]])
    while q:
        idx, value = q.popleft()
        if idx == n-1:
            if value == target:
                answer += 1
            else:
                continue
        else:
            q.append([idx+1, value + numbers[idx+1]])
            q.append([idx+1, value - numbers[idx+1]])
    return answer