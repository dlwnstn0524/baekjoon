from collections import defaultdict

def solution(clothes):
    answer = 1
    clothe_dic = defaultdict(list)
    
    for clothe in clothes:
        clothe_dic[clothe[1]].append(clothe[0])
    
    for key, value in clothe_dic.items():
        answer *= len(value) + 1
    
    return answer-1