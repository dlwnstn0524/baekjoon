from collections import Counter
def solution(clothes):
    clothes_dic = Counter([clothe[1] for clothe in clothes])
    count = 1
    for count_clothes in clothes_dic:
        count = count*(count_clothes + 1)
    return count -1