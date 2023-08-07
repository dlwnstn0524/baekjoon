from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    n = len(begin)
    q = deque()
    q.append([begin, 0])
    while q:
        word, cnt = q.popleft()
        
        for i in range(len(words)):
            temp = 0
            for j in range(n):
                if word[j] == words[i][j]:
                    temp += 1
            if temp == n -1 :
                if words[i] == target:
                    return cnt + 1
                else : 
                    q.append([words[i], cnt + 1])
    