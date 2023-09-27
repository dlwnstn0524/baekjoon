def solution(r1, r2):
    answer = 0
    for i in range(-r2, r2+1):
        for j in range(-r2, r2+1):
            if r1**2 <= (i**2) + (j**2) and (i**2)+(j**2) <= r2**2:
                answer += 1
    return answer