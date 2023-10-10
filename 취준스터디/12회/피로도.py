from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for each_case in permutations(dungeons, len(dungeons)):
        fatigue = k
        count = 0
        for target in each_case:
            if fatigue >= target[0]:
                fatigue -= target[1]
                count += 1
        answer = max(answer, count)
    return answer