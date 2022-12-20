import sys
def solution(s):
    answer = [-1 for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(0, i):
            if s[i] == s[j]:
                answer[i] = i-j
    return answer

s= input()
print(solution(s))