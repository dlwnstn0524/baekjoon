from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for clothe in clothes:
        clothes_dict[clothe[1]].append(clothe[0])
    for value in clothes_dict.values():
        answer *= len(value) + 1
    
    return answer - 1