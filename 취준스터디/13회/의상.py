def solution(clothes):
    answer = 1
    cate_dic = dict()
    for clothe in clothes:
        if clothe[1] not in cate_dic.keys():
            cate_dic[clothe[1]] = [clothe[0]]
        else:
            cate_dic[clothe[1]].append(clothe[0])
    for key in cate_dic.keys():
        answer *= len(cate_dic[key]) + 1
    answer -= 1
    return answer