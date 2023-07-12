def solution(s):
    answer = []
    list_temp = []
    for c in s:
        list_temp.append(c)
    list_temp = list(set(list_temp))
    dict_temp = dict()
    for i in list_temp:
        dict_temp[i] = 0
    for c in s:
        dict_temp[c] += 1
    for key in dict_temp.keys():
        if dict_temp[key] == 1:
            answer.append(key)
            
    answer.sort()
    return ''.join(answer)