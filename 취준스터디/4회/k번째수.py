def solution(array, commands):
    answer = []
    for command in commands:
        cand = array[command[0]-1:command[1]]
        cand.sort()
        answer.append(cand[command[2]-1])
    return answer