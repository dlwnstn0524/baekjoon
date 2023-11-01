from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    
    q.append([numbers[0], 1])
    q.append([-numbers[0], 1])
    
    while q:
        value, idx = q.popleft()
        if idx == n:
            if value == target:
                answer += 1
        else:
            q.append([value+numbers[idx], idx+1])
            q.append([value-numbers[idx], idx+1])
        
    return answer