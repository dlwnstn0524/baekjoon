def solution(participant, completion):
    n = len(completion)
    participant.sort()
    completion.sort()
    for i in range(n):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
    