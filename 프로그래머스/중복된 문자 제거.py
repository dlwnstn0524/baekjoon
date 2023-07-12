def solution(my_string):
    answer = []
    for c in my_string:
        if c not in answer :
            answer.append(c)
    return ''.join(answer)