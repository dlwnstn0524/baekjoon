from collections import deque

def solution(maps):
    answer = 0
    q = deque()
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    return answer