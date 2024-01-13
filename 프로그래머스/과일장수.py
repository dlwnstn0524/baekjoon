def solution(k, m, score):
    answer = 0
    while True: 
        if len(score) < m:
            break
        score.sort(reverse=True)
        answer += min(score[:m])*m
        score = score[m:]
    return answer